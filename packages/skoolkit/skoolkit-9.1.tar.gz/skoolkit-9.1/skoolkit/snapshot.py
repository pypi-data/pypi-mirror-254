# Copyright 2009-2013, 2015-2023 Richard Dymond (rjdymond@gmail.com)
#
# This file is part of SkoolKit.
#
# SkoolKit is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# SkoolKit is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# SkoolKit. If not, see <http://www.gnu.org/licenses/>.

import textwrap
import zlib

from skoolkit import SkoolKitError, get_dword, get_int_param, parse_int, read_bin_file
from skoolkit.components import get_snapshot_reader, get_value

FRAME_DURATIONS = (69888, 70908)

# https://worldofspectrum.net/faq/reference/z80format.htm
Z80_REGISTERS = {
    'a': 0,
    'f': 1,
    'bc': 2,
    'c': 2,
    'b': 3,
    'hl': 4,
    'l': 4,
    'h': 5,
    'sp': 8,
    'i': 10,
    'r': 11,
    'de': 13,
    'e': 13,
    'd': 14,
    '^bc': 15,
    '^c': 15,
    '^b': 16,
    '^de': 17,
    '^e': 17,
    '^d': 18,
    '^hl': 19,
    '^l': 19,
    '^h': 20,
    '^a': 21,
    '^f': 22,
    'iy': 23,
    'ix': 25,
    'pc': 32
}

# https://spectaculator.com/docs/zx-state/z80regs.shtml
SZX_REGISTERS = {
    'a': 1,
    'f': 0,
    'bc': 2,
    'c': 2,
    'b': 3,
    'de': 4,
    'e': 4,
    'd': 5,
    'hl': 6,
    'l': 6,
    'h': 7,
    '^a': 9,
    '^f': 8,
    '^bc': 10,
    '^c': 10,
    '^b': 11,
    '^de': 12,
    '^e': 12,
    '^d': 13,
    '^hl': 14,
    '^l': 14,
    '^h': 15,
    'ix': 16,
    'iy': 18,
    'sp': 20,
    'pc': 22,
    'i': 24,
    'r': 25
}

class Memory:
    def __init__(self, snapshot=None, banks=None, page=None):
        if banks:
            self.banks = banks
            if page is None:
                # Z80 48K
                self.memory = [[0] * 0x4000, self.banks[5], self.banks[1], self.banks[2]]
            else:
                self.memory = [[0] * 0x4000, self.banks[5], self.banks[2], self.banks[page]]
        elif len(snapshot) == 0x20000:
            self.banks = [snapshot[a:a + 0x4000] for a in range(0, 0x20000, 0x4000)]
            self.memory = [[0] * 0x4000, self.banks[5], self.banks[2], self.banks[page]]
        else:
            self.banks = [None] * 8
            self.memory = [[0] * 0x4000, snapshot[0x4000:0x8000], snapshot[0x8000:0xC000], snapshot[0xC000:]]

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.memory[index // 0x4000][index % 0x4000]
        return [self.memory[a // 0x4000][a % 0x4000] for a in range(index.start, min(index.stop, 0x10000))]

    def __setitem__(self, index, value):
        if isinstance(index, int):
            self.memory[index // 0x4000][index % 0x4000] = value
        else:
            for a, b in zip(range(index.start, index.stop), value):
                self.memory[a // 0x4000][a % 0x4000] = b

    def contents(self):
        if all(self.banks):
            return self.banks
        return self.memory[1] + self.memory[2] + self.memory[3]

    def ram(self, page):
        if not all(self.banks) or page is None:
            if self.memory[2]:
                return self.memory[1] + self.memory[2] + self.memory[3]
            return self.memory[1] + [0] * 32768
        if page >= 0:
            return self.banks[5] + self.banks[2] + self.banks[page]
        return self.banks[0] + self.banks[1] + self.banks[2] + self.banks[3] + self.banks[4] + self.banks[5] + self.banks[6] + self.banks[7]

class Snapshot:
    @classmethod
    def get(cls, sfile):
        ext = sfile[-4:].lower()
        if ext == '.sna':
            return SNA(sfile)
        if ext == '.szx':
            return SZX(sfile)
        if ext == '.z80':
            return Z80(sfile)

    def ram(self, page=None):
        return self.memory.ram(page)

    def move(self, specs):
        for spec in specs:
            move(self.memory, spec)

    def poke(self, specs):
        for spec in specs:
            poke(self.memory, spec)

class SNA(Snapshot):
    def __init__(self, snafile):
        banks = [None] * 8
        data = list(read_bin_file(snafile))
        if len(data) > 49179:
            page = data[49181] % 8
            offset = 49183
            for i in sorted(set(range(8)) - {5, 2, page}):
                banks[i] = data[offset:offset + 16384]
                offset += 16384
        else:
            page = 0
        banks[5] = data[27:16411]
        banks[2] = data[16411:32795]
        banks[page] = data[32795:49179]
        self.memory = Memory(banks=banks, page=page)

class SZX(Snapshot):
    def __init__(self, szxfile=None, ram=None):
        if szxfile:
            self._read(szxfile)
        else:
            self.header = bytearray(b'ZXST\x01\x04\x01\x00')
            self.blocks = {}
            if len(ram) == 8:
                # 128K
                self.header[6] = 2
                self.blocks[b'AY\x00\x00'] = bytearray([0] * 18)
                banks = ram
            else:
                # 48K
                self.blocks[b'KEYB'] = bytearray([0] * 5)
                banks = [None] * 8
                banks[5] = ram[0x0000:0x4000]
                banks[2] = ram[0x4000:0x8000]
                banks[0] = ram[0x8000:0xC000]
            self.memory = Memory(banks=banks)

    def _read(self, szxfile):
        self.blocks = {}
        banks = [None] * 8
        data = bytearray(read_bin_file(szxfile))
        if len(data) < 8 or data[:4] != b'ZXST':
            raise SnapshotError(f'{szxfile}: invalid SZX file')
        self.header = data[:8]
        page = 0
        i = 8
        while i + 8 <= len(data):
            block_id = data[i:i + 4]
            block_len = get_dword(data, i + 4)
            if i + 8 + block_len <= len(data):
                if block_id == b'RAMP':
                    bank = data[i + 10] % 8
                    ram = data[i + 11:i + 8 + block_len]
                    if data[i + 8] % 2:
                        try:
                            ram = zlib.decompress(ram)
                        except zlib.error as e:
                            raise SnapshotError(f'Error while decompressing page {bank}: {e.args[0]}')
                    if len(ram) != 16384:
                        raise SnapshotError(f'Page {bank} is {len(ram)} bytes (should be 16384)')
                    banks[bank] = list(ram)
                else:
                    if block_id == b'SPCR':
                        page = data[i + 9] % 8
                    self.blocks[bytes(block_id)] = data[i + 8:i + 8 + block_len]
            i += 8 + block_len
        if self.header[6] > 1 and b'SPCR' not in self.blocks:
            raise SnapshotError("SPECREGS (SPCR) block not found")
        self.memory = Memory(banks=banks, page=page)

    def _add_zxstspecregs(self, state):
        spcr = self.blocks.setdefault(b'SPCR', bytearray([0] * 8))
        for spec in state:
            name, sep, val = spec.lower().partition('=')
            try:
                if name == 'border':
                    spcr[0] = get_int_param(val) % 8
                elif name == '7ffd':
                    spcr[1] = get_int_param(val) % 256
                elif name == 'fe':
                    spcr[3] = get_int_param(val) % 256
            except ValueError:
                raise SkoolKitError(f'Cannot parse integer: {spec}')

    def _add_zxstz80regs(self, registers, state):
        z80r = self.blocks.setdefault(b'Z80R', bytearray([0] * 37))
        for spec in registers:
            reg, sep, val = spec.lower().partition('=')
            if sep:
                if reg.startswith('^'):
                    size = len(reg) - 1
                else:
                    size = len(reg)
                offset = SZX_REGISTERS.get(reg)
                if offset is None:
                    raise SkoolKitError(f'Invalid register: {spec}')
                try:
                    value = get_int_param(val, True)
                except ValueError:
                    raise SkoolKitError(f'Cannot parse register value: {spec}')
                z80r[offset] = value % 256
                if size == 2:
                    z80r[offset + 1] = (value // 256) % 256
        for spec in state:
            name, sep, val = spec.lower().partition('=')
            try:
                if name == 'iff':
                    z80r[26] = z80r[27] = get_int_param(val) & 255
                elif name == 'im':
                    z80r[28] = get_int_param(val) & 3
                elif name == 'tstates':
                    tstates = get_int_param(val)
                    z80r[29:32] = (tstates % 256, (tstates // 256) % 256, (tstates // 65536) % 256)
            except ValueError:
                raise SkoolKitError(f'Cannot parse integer: {spec}')

    def _add_zxstayblock(self, state):
        ay = self.blocks.setdefault(b'AY\x00\x00', bytearray([0] * 18))
        for spec in state:
            name, sep, val = spec.lower().partition('=')
            try:
                if name == 'fffd':
                    ay[1] = get_int_param(val) % 256
                elif name.startswith('ay[') and name.endswith(']'):
                    r = get_int_param(name[3:-1]) % 16
                    ay[2 + r] = get_int_param(val) % 256
            except ValueError:
                raise SkoolKitError(f'Cannot parse integer: {spec}')

    def _add_zxstkeyboard(self, state):
        keyb = self.blocks.setdefault(b'KEYB', bytearray([0] * 5))
        for spec in state:
            name, sep, val = spec.lower().partition('=')
            try:
                if name == 'issue2':
                    keyb[0] = get_int_param(val) % 2
            except ValueError:
                raise SkoolKitError(f'Cannot parse integer: {spec}')

    def _get_zxstrampage(self, page, data):
        ram = zlib.compress(bytes(data), 9)
        size = len(ram) + 3
        ramp = bytearray(b'RAMP')
        ramp.extend((size % 256, size // 256, 0, 0)) # Block size
        ramp.extend((1, 0, page))
        ramp.extend(ram)
        return ramp

    def set_registers_and_state(self, registers, state):
        self._add_zxstspecregs(state)
        self._add_zxstz80regs(registers, state)
        if any(spec.startswith(('ay[', 'fffd=')) for spec in state):
            self._add_zxstayblock(state)
        if any(spec.startswith('issue2=') for spec in state) and self.header[6] < 2:
            self._add_zxstkeyboard(state)

    def write(self, szxfile):
        with open(szxfile, 'wb') as f:
            f.write(self.header)
            for block_id, block_data in self.blocks.items():
                f.write(block_id)
                size = len(block_data)
                f.write(bytes((size % 256, (size >> 8) % 256, (size >> 16) % 256, (size >> 24) % 256)))
                f.write(block_data)
            for bank, data in enumerate(self.memory.banks):
                if data:
                    f.write(self._get_zxstrampage(bank, data))

class Z80(Snapshot):
    def __init__(self, z80file=None, ram=(0,) * 49152):
        if z80file:
            self._read(z80file)
        else:
            self.header = [0] * 86
            self.header[30] = 54 # Version 3
            if len(ram) == 8:
                # 128K
                self.header[34] = 4
                banks = ram
            else:
                # 48K
                banks = [None] * 8
                banks[5] = ram[0x0000:0x4000]
                banks[1] = ram[0x4000:0x8000]
                banks[2] = ram[0x8000:0xC000]
            self.memory = Memory(banks=banks)

    def _read(self, z80file):
        banks = [None] * 8
        data = list(read_bin_file(z80file))
        if sum(data[6:8]) > 0:
            # Version 1
            page = 0
            self.header = data[:30]
            if data[12] & 32:
                ram = self._decompress(data[30:-4])
            else:
                ram = data[30:]
            banks[5] = ram[0x0000:0x4000]
            banks[2] = ram[0x4000:0x8000]
            banks[0] = ram[0x8000:0xC000]
        else:
            page = None
            i = 32 + data[30]
            self.header = data[:i]
            if (i == 55 and data[34] > 2) or (i > 55 and data[34] > 3):
                page = data[35] % 8 # 128K
            while i < len(data):
                length = data[i] + 256 * data[i + 1]
                bank = data[i + 2] - 3
                if length == 65535:
                    length = 16384
                    banks[bank] = data[i + 3:i + 3 + length]
                else:
                    banks[bank] = self._decompress(data[i + 3:i + 3 + length])
                i += 3 + length
        self.memory = Memory(banks=banks, page=page)

    def _decompress(self, ramz):
        block = []
        i = 0
        while i < len(ramz):
            b = ramz[i]
            i += 1
            if b == 237 and i < len(ramz):
                c = ramz[i]
                i += 1
                if c == 237:
                    length, byte = ramz[i], ramz[i + 1]
                    if length == 0:
                        raise SnapshotError("Found ED ED 00 {0:02X}".format(byte))
                    block += [byte] * length
                    i += 2
                else:
                    block += [b, c]
            else:
                block.append(b)
        return block

    def _set_registers(self, specs):
        for spec in specs:
            reg, sep, val = spec.lower().partition('=')
            if sep:
                if reg.startswith('^'):
                    size = len(reg) - 1
                else:
                    size = len(reg)
                if reg == 'pc' and sum(self.header[6:8]) > 0:
                    offset = 6
                else:
                    offset = Z80_REGISTERS.get(reg, -1)
                if offset >= 0:
                    try:
                        value = get_int_param(val, True)
                    except ValueError:
                        raise SkoolKitError("Cannot parse register value: {}".format(spec))
                    lsb, msb = value % 256, (value & 65535) // 256
                    if size == 1:
                        self.header[offset] = lsb
                    elif size == 2:
                        self.header[offset:offset + 2] = [lsb, msb]
                    if reg == 'r':
                        if lsb & 128:
                            self.header[12] |= 1
                        else:
                            self.header[12] &= 254
                else:
                    raise SkoolKitError('Invalid register: {}'.format(spec))

    def _set_state(self, specs):
        for spec in specs:
            name, sep, val = spec.lower().partition('=')
            try:
                if name == 'iff':
                    self.header[27] = self.header[28] = get_int_param(val) & 255
                elif name == 'im':
                    self.header[29] &= 252 # Clear bits 0 and 1
                    self.header[29] |= get_int_param(val) & 3
                elif name == 'issue2':
                    self.header[29] &= 251 # Clear bit 2
                    self.header[29] |= (get_int_param(val) & 1) * 4
                elif name == 'border':
                    self.header[12] &= 241 # Clear bits 1-3
                    self.header[12] |= (get_int_param(val) & 7) * 2 # Border colour
                elif name == 'tstates':
                    frame_duration = FRAME_DURATIONS[self.header[34] > 3]
                    qframe_duration = frame_duration // 4
                    t = frame_duration - 1 - (get_int_param(val) % frame_duration)
                    t1, t2 = t % qframe_duration, t // qframe_duration
                    self.header[55:58] = (t1 % 256, t1 // 256, (2 - t2) % 4)
                elif name == '7ffd':
                    self.header[35] = get_int_param(val) & 255
                elif name == 'fffd':
                    self.header[38] = get_int_param(val) & 255
                elif name.startswith('ay[') and name.endswith(']'):
                    r = get_int_param(name[3:-1]) & 15
                    self.header[39 + r] = get_int_param(val) & 255
            except ValueError:
                raise SkoolKitError("Cannot parse integer: {}".format(spec))

    def _make_z80_ram_block(self, data, page=None):
        block = []
        prev_b = None
        count = 0
        for b in data:
            if b == prev_b or prev_b is None:
                prev_b = b
                if count < 255:
                    count += 1
                    continue
            if count > 4 or (count > 1 and prev_b == 237):
                block.extend((237, 237, count, prev_b))
            elif prev_b == 237:
                block.extend((237, b))
                prev_b = None
                count = 0
                continue
            else:
                block.extend((prev_b,) * count)
            prev_b = b
            count = 1
        if count > 4 or (count > 1 and prev_b == 237):
            block.extend((237, 237, count, prev_b))
        else:
            block.extend((prev_b,) * count)
        if page is None:
            return bytes(block + [0, 237, 237, 0])
        length = len(block)
        return bytes([length % 256, length // 256, page] + block)

    def set_registers_and_state(self, registers, state):
        self._set_registers(registers)
        self._set_state(state)

    def write(self, z80file):
        with open(z80file, 'wb') as f:
            if len(self.header) == 30:
                # Version 1
                self.header[12] |= 32 # RAM is compressed
                f.write(bytes(self.header))
                ram = self.memory.banks[5] + self.memory.banks[2] + self.memory.banks[0]
                f.write(self._make_z80_ram_block(ram))
            else:
                f.write(bytes(self.header))
                for bank, data in enumerate(self.memory.banks, 3):
                    if data:
                        f.write(self._make_z80_ram_block(data, bank))

# Component API
def can_read(fname):
    """
    Return whether this snapshot reader can read the file `fname`.
    """
    return fname[-4:].lower() in ('.sna', '.z80', '.szx')

# Component API
def get_snapshot(fname, page=None):
    """
    Read a snapshot file and produce a list of byte values. For a 48K snapshot,
    or a 128K snapshot with a page number (0-7) specified, the list contains
    65536 (64K) elements: a blank 16K ROM followed by 48K RAM. For a 128K
    snapshot with `page` equal to -1, the list contains 131072 (128K) elements:
    RAM banks 0-7 (16K each) in order.

    :param fname: The snapshot filename.
    :param page: The page number (0-7) to map to addresses 49152-65535
                 (C000-FFFF), or -1 to return all RAM banks. This is relevant
                 only when reading a 128K snapshot file.
    :return: A list of byte values.
    """
    if not can_read(fname):
        raise SnapshotError("{}: Unknown file type".format(fname))
    ram = Snapshot.get(fname).ram(page)
    if len(ram) == 49152:
        return [0] * 16384 + list(ram)
    if len(ram) == 131072:
        return list(ram)
    raise SnapshotError(f'RAM size is {len(ram)}')

def make_snapshot(fname, org, start=None, end=65536, page=None):
    snapshot_reader = get_snapshot_reader()
    if snapshot_reader.can_read(fname):
        if start is None:
            start = parse_int(get_value('DefaultDisassemblyStartAddress'), 16384)
        return snapshot_reader.get_snapshot(fname, page), start, end
    if start is None:
        start = 0
    ram = read_bin_file(fname, 65536)
    if org is None:
        org = 65536 - len(ram)
    mem = [0] * 65536
    mem[org:org + len(ram)] = ram
    return mem, max(org, start), min(end, org + len(ram))

def write_snapshot(fname, ram, registers, state):
    snapshot_type = fname[-4:].lower()
    if snapshot_type == '.z80':
        snapshot = Z80(ram=ram)
        registers = ('i=63', 'iy=23610', *registers)
    elif snapshot_type == '.szx':
        snapshot = SZX(ram=ram)
    else:
        raise SnapshotError(f'{fname}: Unsupported snapshot type')
    snapshot.set_registers_and_state(registers, ('iff=1', 'im=1', 'tstates=34943', *state))
    snapshot.write(fname)

def print_reg_help(short_option=None):
    options = ['--reg name=value']
    if short_option:
        options.insert(0, '-{} name=value'.format(short_option))
    reg_names = ', '.join(sorted(Z80_REGISTERS))
    print("""
Usage: {}

Set the value of a register or register pair. For example:

  --reg hl=32768
  --reg b=17

To set the value of an alternate (shadow) register, use the '^' prefix:

  --reg ^hl=10072

Recognised register names are:

  {}
""".format(', '.join(options), '\n  '.join(textwrap.wrap(reg_names, 70))).strip())

def print_state_help(short_option=None, show_defaults=True):
    options = ['--state name=value']
    if short_option:
        options.insert(0, '-{} name=value'.format(short_option))
    opts = ', '.join(options)
    if show_defaults:
        infix = 'and their default values '
        border = issue2 = ' (default=0)'
        iff = im = ' (default=1)'
        tstates = ' (default=34943)'
    else:
        infix = border = issue2 = iff = im = tstates = ''
    attributes = [
        ('7ffd', 'last OUT to port 0x7ffd (128K only)'),
        ('ay[N]', 'contents of AY register N (N=0-15; 128K only)'),
        ('border', f'border colour{border}'),
        ('fe', 'last OUT to port 0xfe (SZX only)'),
        ('fffd', 'last OUT to port 0xfffd (128K only)'),
        ('iff', f'interrupt flip-flop: 0=disabled, 1=enabled{iff}'),
        ('im', f'interrupt mode{im}'),
        ('issue2', f'issue 2 emulation: 0=disabled, 1=enabled{issue2}'),
        ('tstates', f'T-states elapsed since start of frame{tstates}')
    ]
    attrs = '\n'.join(f'  {a:<7} - {d}' for a, d in sorted(attributes))
    print(f'Usage: {opts}\n\nSet a hardware state attribute. Recognised names {infix}are:\n\n{attrs}')

def _get_page(param, desc, spec, default=None):
    if ':' in param:
        page, v = param.split(':', 1)
        try:
            return get_int_param(page), v
        except ValueError:
            raise SkoolKitError(f'Invalid page number in {desc} spec: {spec}')
    return default, param

def move(snapshot, param_str):
    try:
        src, length, dest = param_str.split(',', 2)
    except ValueError:
        raise SkoolKitError(f'Not enough arguments in move spec (expected 3): {param_str}')
    src_page, src = _get_page(src, 'move', param_str)
    dest_page, dest = _get_page(dest, 'move', param_str, src_page)
    try:
        src, length, dest = [get_int_param(p, True) for p in (src, length, dest)]
    except ValueError:
        raise SkoolKitError('Invalid integer in move spec: {}'.format(param_str))
    if src_page is None:
        snapshot[dest:dest + length] = snapshot[src:src + length]
    elif hasattr(snapshot, 'banks'):
        src_bank = snapshot.banks[src_page % 8]
        dest_bank = snapshot.banks[dest_page % 8]
        if src_bank and dest_bank:
            s = src % 0x4000
            d = dest % 0x4000
            dest_bank[d:d + length] = src_bank[s:s + length]

def poke(snapshot, param_str):
    try:
        addr, val = param_str.split(',', 1)
    except ValueError:
        raise SkoolKitError("Value missing in poke spec: {}".format(param_str))
    page, addr = _get_page(addr, 'poke', param_str)
    try:
        if val.startswith('^'):
            value = get_int_param(val[1:], True)
            poke_f = lambda b: b ^ value
        elif val.startswith('+'):
            value = get_int_param(val[1:], True)
            poke_f = lambda b: (b + value) & 255
        else:
            value = get_int_param(val, True)
            poke_f = lambda b: value
    except ValueError:
        raise SkoolKitError('Invalid value in poke spec: {}'.format(param_str))
    try:
        values = [get_int_param(i, True) for i in addr.split('-', 2)]
    except ValueError:
        raise SkoolKitError('Invalid address range in poke spec: {}'.format(param_str))
    addr1, addr2, step = values + [values[0], 1][len(values) - 1:]
    if page is None:
        for a in range(addr1, addr2 + 1, step):
            snapshot[a] = poke_f(snapshot[a])
    elif hasattr(snapshot, 'banks'):
        bank = snapshot.banks[page % 8]
        if bank:
            for a in range(addr1, addr2 + 1, step):
                bank[a % 0x4000] = poke_f(bank[a % 0x4000])

# API (SnapshotReader)
class SnapshotError(SkoolKitError):
    """Raised when an error occurs while reading a snapshot file."""
