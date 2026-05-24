import sys

class BitString:
    def __init__(self, inp_string=""):
        self.bs = ['0'] * 8

        if inp_string:
            tmps = ['0'] * 8
            i = 0
            while i < 8 and i < len(inp_string):
                c = inp_string[i]
                if c != '0' and c != '1':
                    print("Некорректный символ в строке")
                    sys.exit(0)
                tmps[i] = c
                i += 1
            for j in range(i):
                self.bs[8 - i + j] = tmps[j]

    def input(self):
        tmps = ['0'] * 8
        i = 0
        print("Введите битовую строку: ", end="")
        user_line = sys.stdin.readline()
        for tmp in user_line:
            if i >= 8 or tmp == '\n':
                break
            if tmp != '0' and tmp != '1':
                print("Некорректный ввод")
                sys.exit(0)
            tmps[i] = tmp
            i += 1

        self.bs = ['0'] * 8
        for j in range(i):
            self.bs[8 - i + j] = tmps[j]

    def output(self):
        for j in range(8):
            print(self.bs[j], end="")
        print()

    def conjanction(self, b):  # сохранено оригинальное название
        tmps = []
        for j in range(8):
            tmps.append('1' if (self.bs[j] == '1' and b.bs[j] == '1') else '0')
        return BitString("".join(tmps))

    def fileinput(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
        except Exception:
            print(f"Ошибка: файл {filename} не открыт")
            sys.exit(0)

        tmps = ['0'] * 8
        i = 0
        for tmp in content:
            if i >= 8:
                break
            if tmp == '0' or tmp == '1':
                tmps[i] = tmp
                i += 1

        self.bs = ['0'] * 8
        for j in range(i):
            self.bs[8 - i + j] = tmps[j]

    def fileoutput(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            for j in range(8):
                file.write(self.bs[j])