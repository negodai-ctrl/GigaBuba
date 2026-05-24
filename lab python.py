import sys
from BitString import BitString


def main():
    print("проверка конкструкторов")

    print("\n1. Конструктор по умолчанию:")
    a = BitString()
    print("a = ", end="")
    a.output()

    print("\n2. Конструктор с параметром:")
    b = BitString("1010")
    print("b = ", end="")
    b.output()

    print("\n3. Конструктор копирования:")
    c = BitString()
    c = BitString("".join(b.bs))
    print("c (копия b) = ", end="")
    c.output()

    print("\n4. Ввод строки 1 с консоли:")
    d = BitString()
    d.input()
    print("d = ", end="")
    d.output()

    print("\n5. Чтение строки 2 из файла b.txt:")
    e = BitString()
    e.fileinput("b.txt")
    print("e = ", end="")
    e.output()

    print("\n6. Конъюнкция d AND e:")
    f = d.conjanction(e)
    print("f = ", end="")
    f.output()

    print("\n7. Сохранение в c.txt...")
    f.fileoutput("c.txt")
    print("Готово!")

    print("\n8. Оператор присваивания:")
    g = BitString()
    g = f
    print("g = f = ", end="")
    g.output()
    input("Нажмите Enter для выхода...")


if __name__ == "__main__":
    main()