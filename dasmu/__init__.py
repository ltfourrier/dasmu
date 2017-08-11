import sys

from dasmu import assembler as asm
from dasmu import disassembler as dasm


def main():
    with open(sys.argv[1], 'rb') as file:
        data = file.read()
        lexer = dasm.Lexer(data)
        while lexer.current_byte is not None:
            print('0x{:02x}'.format(lexer.current_byte))
            print('Byte count: {0}'.format(dasm.get_inst_byte_count(lexer.current_byte)))
            lexer.get_next_byte()


if __name__ == '__main__':
    main()
