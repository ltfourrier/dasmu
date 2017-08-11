def get_inst_byte_count(byte):
    hi, lo = byte >> 4, byte & 0xF
    if lo == 0x0:
        if hi in (0x0, 0x4, 0x6,):
            return 1
        elif hi == 0x2:
            return 3
        else:
            return 2
    elif lo == 0x9:
        return 3 if hi & 1 == 1 else 2
    elif lo in (0x8, 0xA,):
        return 1
    elif lo in (0xC, 0xD, 0xE):
        return 3
    else:
        return 2


class Lexer(object):
    def __init__(self, data):
        self._data = data
        self._cursor = 0
        self.current_byte = self._data[self._cursor]
        self.current_token = None

    def _read_byte(self):
        if self._cursor + 1 >= len(self._data):
            return None
        self._cursor += 1
        return self._data[self._cursor]

    def get_next_byte(self):
        self.current_byte = self._read_byte()
        return self.current_byte
