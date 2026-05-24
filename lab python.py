import sys
import locale
from BitString import BitString

def main():
    a = BitString()
    b = BitString()
    c = BitString()

    a.input()
    print("Чтение строки 2 из файла b.txt...")
    b.fileinput("b.txt")
    print("Строка 1: ", end="")
    a.output()
    print("Строка 2: ", end="")
    b.output()
    c = a.conjanction(b)
    print("Результат (AND): ", end="")
    c.output()
    print("Сохранение в c.txt...")
    c.fileoutput("c.txt")

if __name__ == "__main__":
    main()