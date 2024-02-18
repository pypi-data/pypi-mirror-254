# Copyright 2013-2017, 2019-2023 Richard Dymond (rjdymond@gmail.com)
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

import argparse

from skoolkit import SkoolKitError, get_dword, get_int_param, get_word, integer, read_bin_file, VERSION
from skoolkit.basic import BasicLister, VariableLister, get_char
from skoolkit.config import get_config, show_config, update_options
from skoolkit.opcodes import END, decode
from skoolkit.snapshot import FRAME_DURATIONS, make_snapshot
from skoolkit.sna2skool import get_ctl_parser
from skoolkit.snaskool import Disassembly

class Registers:
    def __init__(self, a=0, f=0, bc=0, de=0, hl=0, a2=0, f2=0, bc2=0, de2=0, hl2=0,
                 ix=0, iy=0, sp=0, i=0, r=0, pc=0, border=0, iff2=0, im=0,
                 tstates=0, out7ffd=0, outfffd=0, ay=(0,) * 16, outfe=0):
        self.a = a
        self.f = f
        self.bc = bc
        self.de = de
        self.hl = hl
        self.a2 = a2
        self.f2 = f2
        self.bc2 = bc2
        self.de2 = de2
        self.hl2 = hl2
        self.ix = ix
        self.iy = iy
        self.sp = sp
        self.i = i
        self.r = r
        self.pc = pc
        self.border = border
        self.iff2 = iff2
        self.im = im
        self.tstates = tstates
        self.out7ffd = out7ffd
        self.outfffd = outfffd
        self.ay = ay
        self.outfe = outfe
        self.reg_map = {
            'b': 'bc', 'c': 'bc', 'b2': 'bc2', 'c2': 'bc2',
            'd': 'de', 'e': 'de', 'd2': 'de2', 'e2': 'de2',
            'h': 'hl', 'l': 'hl', 'h2': 'hl2', 'l2': 'hl2'
        }

    def get_lines(self):
        lines = []
        sep = ' ' * 4
        for row in (
            ('pc', 'sp'), ('ix', 'iy'), ('i', 'r'),
            ('b', 'b2'), ('c', 'c2'), ('bc', 'bc2'),
            ('d', 'd2'), ('e', 'e2'), ('de', 'de2'),
            ('h', 'h2'), ('l', 'l2'), ('hl', 'hl2'),
            ('a', 'a2')
        ):
            lines.append(self._reg(sep, *row))
        lines.append("  {0}    {1}   {0}".format("SZ5H3PNC", sep))
        lines.append("F {:08b}    {}F' {:08b}".format(self.f, sep, self.f2))
        return lines

    def _reg(self, sep, *registers):
        strings = []
        for reg in registers:
            name = reg.upper().replace('2', "'")
            size = len(name) - 1 if name.endswith("'") else len(name)
            value = self._get_value(reg)
            strings.append("{0:<3} {1:>5} {2:<{3}}{1:0{4}X}".format(name, value, "", (2 - size) * 2, size * 2))
        return sep.join(strings)

    def _get_value(self, register):
        try:
            return getattr(self, register)
        except AttributeError:
            reg_pair = self.reg_map[register]
            word = getattr(self, reg_pair)
            if register[0] == reg_pair[0]:
                return word // 256
            return word % 256

def parse_snapshot(infile):
    snapshot_type = infile[-4:].lower()
    if snapshot_type == '.sna':
        return _parse_sna(infile)
    if snapshot_type == '.z80':
        return _parse_z80(infile)
    if snapshot_type == '.szx':
        return _parse_szx(infile)
    return None, None, None

###############################################################################

# https://worldofspectrum.net/features/faq/reference/z80format.htm
# https://worldofspectrum.net/features/faq/reference/128kreference.htm

BLOCK_ADDRESSES_48K = {
    4: '32768-49151 8000-BFFF',
    5: '49152-65535 C000-FFFF',
    8: '16384-32767 4000-7FFF'
}

BLOCK_ADDRESSES_128K = {
    5: '32768-49151 8000-BFFF',
    8: '16384-32767 4000-7FFF'
}

V2_MACHINES = {
    0: ('48K Spectrum', '16K Spectrum', True),
    1: ('48K Spectrum + IF1', '16K Spectrum + IF1', True),
    2: ('SamRam', 'SamRam', False),
    3: ('128K Spectrum', 'Spectrum +2', False),
    4: ('128K Spectrum + IF1', 'Spectrum +2 + IF1', False)
}

V3_MACHINES = {
    0: ('48K Spectrum', '16K Spectrum', True),
    1: ('48K Spectrum + IF1', '16K Spectrum + IF1', True),
    2: ('SamRam', 'SamRam', False),
    3: ('48K Spectrum + MGT', '16K Spectrum + MGT', True),
    4: ('128K Spectrum', 'Spectrum +2', False),
    5: ('128K Spectrum + IF1', 'Spectrum +2 + IF1', False),
    6: ('128K Spectrum + MGT', 'Spectrum +2 + MGT', False),
}

MACHINES = {
    7: ('Spectrum +3', 'Spectrum +2A', False),
    8: ('Spectrum +3', 'Spectrum +2A', False),
    9: ('Pentagon (128K)', 'Pentagon (128K)', False),
    10: ('Scorpion (256K)', 'Scorpion (256K)', False),
    11: ('Didaktik+Kompakt', 'Didaktik+Kompakt', False),
    12: ('Spectrum +2', 'Spectrum +2', False),
    13: ('Spectrum +2A', 'Spectrum +2A', False),
    14: ('TC2048', 'TC2048', False),
    15: ('TC2068', 'TC2068', False),
    128: ('TS2068', 'TS2068', False),
}

def _parse_z80(z80file):
    data = read_bin_file(z80file)

    # Extract header and RAM block(s)
    if get_word(data, 6) > 0:
        version = 1
        header = data[:30]
        ram_blocks = data[30:]
    else:
        header_len = 32 + get_word(data, 30)
        header = data[:header_len]
        ram_blocks = data[header_len:]
        version = 2 if header_len == 55 else 3

    reg = Registers(
        a=header[0],
        f=header[1],
        bc=get_word(header, 2),
        hl=get_word(header, 4),
        sp=get_word(header, 8),
        i=header[10],
        r=128 * (header[12] & 1) + (header[11] & 127),
        de=get_word(header, 13),
        bc2=get_word(header, 15),
        de2=get_word(header, 17),
        hl2=get_word(header, 19),
        a2=header[21],
        f2=header[22],
        iy=get_word(header, 23),
        ix=get_word(header, 25),
        border=(header[12] // 2) % 8,
        iff2=header[28],
        im=header[29] & 3
    )

    if version == 1:
        reg.pc = get_word(header, 6)
    else:
        reg.pc = get_word(header, 32)
        reg.out7ffd = header[35]
        reg.outfffd = header[38]
        reg.ay = tuple(header[39:55])

    if version == 3:
        frame_duration = FRAME_DURATIONS[header[34] > 3]
        qframe_duration = frame_duration // 4
        t1 = (header[55] + 256 * header[56]) % qframe_duration
        t2 = (2 - header[57]) % 4
        reg.tstates = frame_duration - 1 - t2 * qframe_duration - t1

    return header, reg, ram_blocks

def _analyse_z80(z80file, header, reg, ram_blocks):
    if get_word(header, 6) > 0:
        version = 1
    else:
        version = 2 if len(header) == 55 else 3

    # Print file name, version, machine, interrupt status, border, port $7FFD
    print('Z80 file: {}'.format(z80file))
    print('Version: {}'.format(version))
    is128 = False
    if version == 1:
        machine = '48K Spectrum'
        block_dict = BLOCK_ADDRESSES_48K
    else:
        machine_dict = V2_MACHINES if version == 2 else V3_MACHINES
        machine_id = header[34]
        index = header[37] // 128
        machine_spec = machine_dict.get(machine_id, MACHINES.get(machine_id, ('Unknown', 'Unknown', True)))
        machine = machine_spec[index]
        if machine_spec[2]:
            block_dict = BLOCK_ADDRESSES_48K
        else:
            is128 = True
            block_dict = BLOCK_ADDRESSES_128K
    print('Machine: {}'.format(machine))
    print('Interrupts: {}abled'.format('en' if reg.iff2 else 'dis'))
    print('Interrupt mode: {}'.format(reg.im))
    print('Issue 2 emulation: {}abled'.format('en' if header[29] & 4 else 'dis'))
    if version == 3:
        print(f'T-states: {reg.tstates}')
    print('Border: {}'.format((header[12] // 2) & 7))
    if is128:
        print(f'Port $FFFD: {reg.outfffd}')
        bank = header[35] & 7
        print('Port $7FFD: {} - bank {} (block {}) paged into 49152-65535 C000-FFFF'.format(reg.out7ffd, bank, bank + 3))

    # Print register contents
    print('Registers:')
    for line in reg.get_lines():
        print('  ' + line)

    # Print RAM block info
    if version == 1:
        block_len = len(ram_blocks)
        prefix = '' if header[12] & 32 else 'un'
        print('48K RAM block (16384-65535 4000-FFFF): {} bytes ({}compressed)'.format(block_len, prefix))
    else:
        i = 0
        while i < len(ram_blocks):
            block_len = get_word(ram_blocks, i)
            page_num = ram_blocks[i + 2]
            addr_range = block_dict.get(page_num)
            if addr_range is None and page_num - 3 == bank:
                addr_range = '49152-65535 C000-FFFF'
            if addr_range:
                addr_range = ' ({})'.format(addr_range)
            else:
                addr_range = ''
            i += 3
            if block_len == 65535:
                block_len = 16384
                prefix = 'un'
            else:
                prefix = ''
            print('RAM block {}{}: {} bytes ({}compressed)'.format(page_num, addr_range, block_len, prefix))
            i += block_len

###############################################################################

# https://www.spectaculator.com/docs/zx-state/intro.shtml

SZX_MACHINES = {
    0: '16K ZX Spectrum',
    1: '48K ZX Spectrum',
    2: 'ZX Spectrum 128',
    3: 'ZX Spectrum +2',
    4: 'ZX Spectrum +2A/+2B',
    5: 'ZX Spectrum +3',
    6: 'ZX Spectrum +3e'
}

def _parse_szx(szxfile):
    szx = read_bin_file(szxfile)
    magic = _get_block_id(szx, 0)
    if magic != 'ZXST':
        raise SkoolKitError("{} is not an SZX file".format(szxfile))

    header = szx[:8]

    reg = Registers()
    blocks = []
    i = 8
    while i < len(szx):
        block_id = _get_block_id(szx, i)
        block_size = get_dword(szx, i + 4)
        i += 8 + block_size
        block = szx[i - block_size:i]
        blocks.append((block_id, block))
        if block_id == 'Z80R':
            reg.f = block[0]
            reg.a = block[1]
            reg.bc = get_word(block, 2)
            reg.de = get_word(block, 4)
            reg.hl = get_word(block, 6)
            reg.f2 = block[8]
            reg.a2 = block[9]
            reg.bc2 = get_word(block, 10)
            reg.de2 = get_word(block, 12)
            reg.hl2 = get_word(block, 14)
            reg.ix = get_word(block, 16)
            reg.iy = get_word(block, 18)
            reg.sp = get_word(block, 20)
            reg.pc = get_word(block, 22)
            reg.i = block[24]
            reg.r = block[25]
            reg.iff2 = block[27]
            reg.im = block[28]
            reg.tstates = get_dword(block, 29)
        elif block_id == 'SPCR':
            reg.border = block[0]
            reg.out7ffd = block[1]
            reg.outfe = block[3]
        elif block_id == 'AY':
            reg.outfffd = block[1]
            reg.ay = tuple(block[2:18])

    return header, reg, blocks

def _get_block_id(data, index):
    return ''.join(chr(b) for b in data[index:index+ 4] if b)

def _print_ay(block, reg):
    return [f'Current AY register: {reg.outfffd}']

def _print_keyb(block, reg):
    issue2 = get_dword(block, 0) & 1
    return ['Issue 2 emulation: {}abled'.format('en' if issue2 else 'dis')]

def _print_ramp(block, reg):
    flags = get_word(block, 0)
    compressed = 'compressed' if flags & 1 else 'uncompressed'
    page = block[2]
    ram = block[3:]
    addresses = ''
    if page == 5:
        addresses = '16384-32767 4000-7FFF'
    elif page == 2:
        addresses = '32768-49151 8000-BFFF'
    elif reg.machine_id > 1 and page == reg.out7ffd & 7:
        addresses = '49152-65535 C000-FFFF'
    if addresses:
        addresses += ': '
    return (
        f'Page: {page}',
        f'RAM: {addresses}{len(ram)} bytes, {compressed}'
    )

def _print_spcr(block, reg):
    lines = [f'Border: {reg.border}']
    if reg.machine_id > 1:
        lines.append(f'Port $7FFD: {reg.out7ffd} (bank {reg.out7ffd % 8} paged into 49152-65535 C000-FFFF)')
    return lines

def _print_z80r(block, reg):
    lines = [
        'Interrupts: {}abled'.format('en' if reg.iff2 else 'dis'),
        f'Interrupt mode: {reg.im}',
        f'T-states: {reg.tstates}'
    ]
    return lines + reg.get_lines()

SZX_BLOCK_PRINTERS = {
    'AY': _print_ay,
    'KEYB': _print_keyb,
    'RAMP': _print_ramp,
    'SPCR': _print_spcr,
    'Z80R': _print_z80r
}

def _analyse_szx(header, reg, blocks):
    print('Version: {}.{}'.format(header[4], header[5]))
    reg.machine_id = header[6]
    print('Machine: {}'.format(SZX_MACHINES.get(reg.machine_id, 'Unknown')))

    for block_id, block in blocks:
        print('{}: {} bytes'.format(block_id, len(block)))
        printer = SZX_BLOCK_PRINTERS.get(block_id)
        if printer:
            for line in printer(block, reg):
                print("  " + line)

###############################################################################

# https://worldofspectrum.net/features/faq/reference/formats.htm#SNA

def _parse_sna(snafile):
    sna = read_bin_file(snafile, 147488)
    if len(sna) not in (49179, 131103, 147487):
        raise SkoolKitError('{}: not a SNA file'.format(snafile))

    reg = Registers(
        i=sna[0],
        hl2=get_word(sna, 1),
        de2=get_word(sna, 3),
        bc2=get_word(sna, 5),
        f2=sna[7],
        a2=sna[8],
        hl=get_word(sna, 9),
        de=get_word(sna, 11),
        bc=get_word(sna, 13),
        iy=get_word(sna, 15),
        ix=get_word(sna, 17),
        r=sna[20],
        f=sna[21],
        a=sna[22],
        sp=get_word(sna, 23),
        border=sna[26],
        iff2=(sna[19] & 4) // 4,
        im=sna[25]
    )

    if len(sna) > 49179:
        reg.pc = get_word(sna, 49179)
        reg.out7ffd = sna[49181]
    else:
        reg.pc = get_word(sna, reg.sp - 16357)

    return sna[:27], reg, sna[27:]

def _print_ram_banks(sna):
    bank = sna[49154] & 7
    print('RAM bank 5 (16384 bytes: 16384-32767 4000-7FFF)')
    print('RAM bank 2 (16384 bytes: 32768-49151 8000-BFFF)')
    print('RAM bank {} (16384 bytes: 49152-65535 C000-FFFF)'.format(bank))
    for b in sorted({0, 1, 3, 4, 6, 7} - {bank}):
        print('RAM bank {} (16384 bytes)'.format(b))

def _analyse_sna(header, reg, ram):
    is128 = len(ram) > 49152
    print('RAM: {}K'.format(128 if is128 else 48))
    print('Interrupts: {}abled'.format('en' if reg.iff2 else 'dis'))
    print('Interrupt mode: {}'.format(reg.im))
    print('Border: {}'.format(header[26] & 7))

    print('Registers:')
    for line in reg.get_lines():
        print('  ' + line)

    if is128:
        _print_ram_banks(ram)

###############################################################################

def _get_address_ranges(specs, step=1):
    addr_ranges = []
    for addr_range in specs:
        try:
            values = [get_int_param(i, True) for i in addr_range.split('-', 2)]
        except ValueError:
            raise SkoolKitError('Invalid address range: {}'.format(addr_range))
        addr_ranges.append(values + [values[0], step][len(values) - 1:])
    return addr_ranges

def _call_graph(snapshot, ctlfiles, prefix, start, end, config):
    disassembly = Disassembly(snapshot, get_ctl_parser(ctlfiles, prefix, start, end, start, end), self_refs=True)
    entries = {e.address: (e, set(), set(), set(), {}) for e in disassembly.entries if e.ctl == 'c'}
    for entry, children, parents, main_refs, props in entries.values():
        props.update({'address': entry.address, 'label': entry.instructions[0].label or ''})
        for instruction in entry.instructions:
            for ref_addr in instruction.referrers:
                if ref_addr in entries:
                    if ref_addr != entry.address:
                        parents.add(ref_addr)
                        entries[ref_addr][1].add(entry.address)
                    if entry.address == instruction.address:
                        main_refs.add(ref_addr)
        addr, size, mc, op_id, op = next(decode(snapshot, entry.instructions[-1].address, 65536))
        if op_id != END:
            next_entry_addr = addr + size
            if next_entry_addr in entries:
                children.add(next_entry_addr)
                entries[next_entry_addr][2].add(entry.address)
                entries[next_entry_addr][3].add(entry.address)

    for desc, addresses in (
            ('Unconnected', {e.address for e, c, p, m, n in entries.values() if not (c or p)}),
            ('Orphans', {e.address for e, c, p, m, n in entries.values() if c and not p}),
            ('First instruction not used', {e.address for e, c, p, m, n in entries.values() if p and not m})
    ):
        node_ids = [config['NodeId'].format(**entries[addr][4]) for addr in sorted(addresses)]
        if not node_ids:
            node_ids.append('None')
        print('// {}: {}'.format(desc, ', '.join(node_ids)))
    print('digraph {')
    if config['GraphAttributes']:
        print('graph [{}]'.format(config['GraphAttributes']))
    if config['NodeAttributes']:
        print('node [{}]'.format(config['NodeAttributes']))
    if config['EdgeAttributes']:
        print('edge [{}]'.format(config['EdgeAttributes']))
    for entry, children, parents, main_refs, props in entries.values():
        node_id = config['NodeId'].format(**props)
        print('{} [label={}]'.format(node_id, config['NodeLabel'].format(**props)))
        if children:
            ref_ids = [config['NodeId'].format(address=a, label=entries[a][0].instructions[0].label or '') for a in children]
            print('{} -> {{{}}}'.format(node_id, ' '.join(ref_ids)))
    print('}')

def _find(snapshot, byte_seq, base_addr):
    steps = '1'
    if '-' in byte_seq:
        byte_seq, steps = byte_seq.split('-', 1)
    try:
        byte_values = [get_int_param(i, True) for i in byte_seq.split(',')]
    except ValueError:
        raise SkoolKitError('Invalid byte sequence: {}'.format(byte_seq))
    try:
        if '-' in steps:
            limits = [get_int_param(n, True) for n in steps.split('-', 1)]
            steps = range(limits[0], limits[1] + 1)
        else:
            steps = [get_int_param(steps, True)]
    except ValueError:
        raise SkoolKitError('Invalid distance: {}'.format(steps))
    for step in steps:
        offset = step * len(byte_values)
        for a in range(base_addr, 65537 - offset):
            if snapshot[a:a + offset:step] == byte_values:
                print("{0}-{1}-{2} {0:04X}-{1:04X}-{2:X}: {3}".format(a, a + offset - step, step, byte_seq))

def _find_tile(snapshot, coords):
    steps = '1'
    if '-' in coords:
        coords, steps = coords.split('-', 1)
    try:
        x, y = [get_int_param(i) for i in coords.split(',', 1)]
        if not 0 <= x < 32 or not 0 <= y < 24:
            raise ValueError
    except ValueError:
        raise SkoolKitError('Invalid tile coordinates: {}'.format(coords))
    df_addr = 16384 + 2048 * (y // 8) + 32 * (y & 7) + x
    byte_seq = snapshot[df_addr:df_addr + 2048:256]
    for b in byte_seq:
        print('|{:08b}|'.format(b).replace('0', ' ').replace('1', '*'))
    _find(snapshot, '{}-{}'.format(','.join([str(b) for b in byte_seq]), steps), 23296)

def _find_text(snapshot, text, base_addr):
    size = len(text)
    byte_values = [ord(c) for c in text]
    for a in range(base_addr, 65536 - size + 1):
        if snapshot[a:a + size] == byte_values:
            print("{0}-{1} {0:04X}-{1:04X}: {2}".format(a, a + size - 1, text))

def _peek(snapshot, specs, fmt):
    for addr1, addr2, step in _get_address_ranges(specs):
        for a in range(addr1, addr2 + 1, step):
            value = snapshot[a]
            char = get_char(value, '', 'UDG-{}', True)
            print(fmt.format(address=a, value=value, char=char))

def _word(snapshot, specs, fmt):
    for addr1, addr2, step in _get_address_ranges(specs, 2):
        for a in range(addr1, addr2 + 1, step):
            value = snapshot[a] + 256 * snapshot[a + 1]
            print(fmt.format(address=a, value=value))

def run(infile, options, config):
    if any((options.find, options.tile, options.text, options.call_graph, options.peek,
            options.word, options.basic, options.variables)):
        snapshot, start, end = make_snapshot(infile, options.org, page=options.page)
        if options.find:
            _find(snapshot, options.find, start)
        elif options.tile:
            _find_tile(snapshot, options.tile)
        elif options.text:
            _find_text(snapshot, options.text, start)
        elif options.call_graph:
            _call_graph(snapshot, options.ctlfiles, infile, start, end, config)
        elif options.peek:
            _peek(snapshot, options.peek, config['Peek'])
        elif options.word:
            _word(snapshot, options.word, config['Word'])
        else:
            if options.basic:
                print(BasicLister().list_basic(snapshot))
            if options.variables:
                print(VariableLister().list_variables(snapshot))
    else:
        snapshot_type = infile[-4:].lower()
        if snapshot_type == '.sna':
            _analyse_sna(*_parse_sna(infile))
        elif snapshot_type == '.z80':
            _analyse_z80(infile, *_parse_z80(infile))
        elif snapshot_type == '.szx':
            _analyse_szx(*_parse_szx(infile))

def main(args):
    config = get_config('snapinfo')
    parser = argparse.ArgumentParser(
        usage='snapinfo.py [options] file',
        description="Analyse a binary (raw memory) file or a SNA, SZX or Z80 snapshot.",
        add_help=False
    )
    parser.add_argument('infile', help=argparse.SUPPRESS, nargs='?')
    group = parser.add_argument_group('Options')
    group.add_argument('-b', '--basic', action='store_true',
                       help='List the BASIC program.')
    group.add_argument('-c', '--ctl', dest='ctlfiles', metavar='PATH', action='append', default=[],
                       help="When generating a call graph, specify a control file to use, or a directory from which to read control files. "
                            "PATH may be '-' for standard input. This option may be used multiple times.")
    group.add_argument('-f', '--find', metavar='A[,B...[-M[-N]]]',
                       help='Search for the byte sequence A,B... with distance ranging from M to N (default=1) between bytes.')
    group.add_argument('-g', '--call-graph', action='store_true',
                       help='Generate a call graph in DOT format.')
    group.add_argument('-I', '--ini', dest='params', metavar='p=v', action='append', default=[],
                       help="Set the value of the configuration parameter 'p' to 'v'. This option may be used multiple times.")
    group.add_argument('-o', '--org', dest='org', metavar='ADDR', type=integer,
                       help='Specify the origin address of a binary (raw memory) file (default: 65536 - length).')
    group.add_argument('-p', '--peek', metavar='A[-B[-C]]', action='append',
                       help='Show the contents of addresses A TO B STEP C. This option may be used multiple times.')
    group.add_argument('-P', '--page', dest='page', metavar='PAGE', type=int, choices=list(range(8)),
                       help='Specify the page (0-7) of a 128K snapshot to map to 49152-65535.')
    group.add_argument('--show-config', dest='show_config', action='store_true',
                       help="Show configuration parameter values.")
    group.add_argument('-t', '--find-text', dest='text', metavar='TEXT',
                       help='Search for a text string.')
    group.add_argument('-T', '--find-tile', dest='tile', metavar='X,Y[-M[-N]]',
                       help='Search for the graphic data of the tile at (X,Y) with distance ranging from M to N (default=1) between bytes.')
    group.add_argument('-v', '--variables', action='store_true',
                       help='List variables.')
    group.add_argument('-V', '--version', action='version', version='SkoolKit {}'.format(VERSION),
                       help='Show SkoolKit version number and exit.')
    group.add_argument('-w', '--word', metavar='A[-B[-C]]', action='append',
                       help='Show the words at addresses A TO B STEP C. This option may be used multiple times.')
    namespace, unknown_args = parser.parse_known_args(args)
    if namespace.show_config:
        show_config('snapinfo', config)
    if unknown_args or namespace.infile is None:
        parser.exit(2, parser.format_help())
    update_options('snapinfo', namespace, namespace.params, config)
    run(namespace.infile, namespace, config)
