import sys


class BitStringException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.msg = message

    def __str__(self):
        return self.msg


class BitString:
    def __init__(self, inp_string=""):
        self.size = 8
        self.bs = ['0'] * self.size

        if inp_string:
            tmps = ['0'] * self.size
            i = 0
            length = len(inp_string) if len(inp_string) < self.size else self.size

            while i < length:
                c = inp_string[i]
                if c != '0' and c != '1':
                    raise BitStringException(f"Некорректный символ в строке: '{c}'")
                tmps[i] = c
                i += 1

            for j in range(self.size):
                self.bs[j] = '0'
            for j in range(i):
                self.bs[self.size - i + j] = tmps[j]

    def input(self):
        tmps = ['0'] * self.size
        i = 0

        print("Введите битовую строку : ", end="")
        user_line = sys.stdin.readline()
        for tmp in user_line:
            if i >= self.size or tmp == '\n':
                break
            if tmp != '0' and tmp != '1':
                raise BitStringException(f"Некорректный ввод: недопустимый символ '{tmp}'")
            tmps[i] = tmp
            i += 1

        for j in range(self.size):
            self.bs[j] = '0'
        for j in range(i):
            self.bs[self.size - i + j] = tmps[j]

    def output(self):
        for j in range(self.size):
            print(self.bs[j], end="")
        print()

    def conjanction(self, b):
        result = BitString()
        for j in range(self.size):
            result.bs[j] = '1' if (self.bs[j] == '1' and b.bs[j] == '1') else '0'
        return result

    def fileinput(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
        except Exception:
            raise BitStringException(f"Не удалось открыть файл: {filename}")

        tmps = ['0'] * self.size
        i = 0
        hasBits = False
        for tmp in content:
            if i >= self.size:
                break
            if tmp == '0' or tmp == '1':
                tmps[i] = tmp
                i += 1
                hasBits = True

        if not hasBits:
            raise BitStringException(f"Файл '{filename}' не содержит битов (0 или 1)")

        for j in range(self.size):
            self.bs[j] = '0'
        for j in range(i):
            self.bs[self.size - i + j] = tmps[j]

    def fileoutput(self, filename):
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                for j in range(self.size):
                    file.write(self.bs[j])
        except Exception:
            raise BitStringException(f"Не удалось создать файл для записи: {filename}")