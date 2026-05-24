import sys

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
                    print(f"Некорректный символ в строке: {c}")
                    sys.exit(0)
                tmps[i] = c
                i += 1

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
                print("Некорректный ввод")
                sys.exit(0)
            tmps[i] = tmp
            i += 1

        self.bs = ['0'] * self.size
        for j in range(i):
            self.bs[self.size - i + j] = tmps[j]

    def output(self):
        for j in range(self.size):
            print(self.bs[j], end="")
        print()

    def conjanction(self, b):
        result = BitString()
        for j in range(self.size):
            if (self.bs[j] == '1') and (b.bs[j] == '1'):
                result.bs[j] = '1'
            else:
                result.bs[j] = '0'
        return result

    def fileinput(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
        except Exception:
            print(f"Ошибка: файл {filename} не открыт")
            sys.exit(0)

        tmps = ['0'] * self.size
        i = 0
        for tmp in content:
            if i >= self.size:
                break
            if tmp == '0' or tmp == '1':
                tmps[i] = tmp
                i += 1

        self.bs = ['0'] * self.size
        for j in range(i):
            self.bs[self.size - i + j] = tmps[j]

    def fileoutput(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            for j in range(self.size):
                file.write(self.bs[j])
