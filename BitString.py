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
            length = min(len(inp_string), self.size)
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

    # Перегрузка операций
    # Присваивание: a = b
    def __copy__(self):
        """Создает копию объекта"""
        new_obj = BitString()
        new_obj.bs = self.bs[:]
        return new_obj

    # Конъюнкция (логическое И): a & b
    def __and__(self, other):
        """Оператор & — побитовая конъюнкция (AND)"""
        result = BitString()
        for j in range(self.size):
            result.bs[j] = '1' if (self.bs[j] == '1' and other.bs[j] == '1') else '0'
        return result

    # Доступ по индексу: чтение a[3]
    def __getitem__(self, index):
        """Оператор [] — чтение бита"""
        if index < 0 or index >= self.size:
            raise BitStringException("Выход за пределы битовой строки")
        return self.bs[index]

    # Доступ по индексу: запись a[3] = '1'
    def __setitem__(self, index, value):
        """Оператор [] — запись бита"""
        if index < 0 or index >= self.size:
            raise BitStringException("Выход за пределы битовой строки")
        if value not in ('0', '1'):
            raise BitStringException("Можно записать только '0' или '1'")
        self.bs[index] = value

    def __str__(self):
        """Оператор str() / print()"""
        return ''.join(self.bs)

    #  Старое

    def input(self):
        tmps = ['0'] * self.size
        i = 0
        print("Введите битовую строку : ", end="")
        user_line = sys.stdin.readline()
        for tmp in user_line:
            if i >= self.size or tmp == '\n':
                break
            if tmp not in ('0', '1'):
                raise BitStringException(f"Некорректный ввод: недопустимый символ '{tmp}'")
            tmps[i] = tmp
            i += 1
        for j in range(self.size):
            self.bs[j] = '0'
        for j in range(i):
            self.bs[self.size - i + j] = tmps[j]

    def output(self):
        print(self)

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
            if tmp in ('0', '1'):
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
                file.write(str(self))
        except Exception:
            raise BitStringException(f"Не удалось создать файл для записи: {filename}")