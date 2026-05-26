
import sys
from BitString import BitString, BitStringException

def main():
    try:
        print("=== Проверка BitString с перегрузками ===\n")

        a = BitString("10110110")
        b = BitString("11001101")

        print("a =", a)                    # __str__
        print("b =", b)

        c = a & b                          # __and__
        print("a & b =", c)

        print("a[2] =", a[2])              # __getitem__
        a[3] = '1'                         # __setitem__
        print("a после a[3] = '1' →", a)

        print("\nВведите битовую строку:")
        d = BitString()
        d.input()                          # можно оставить input(), т.к. >> в Python нестандартно
        print("Вы ввели:", d)

        e = BitString()
        e = d                              # присваивание
        print("e = d →", e)

    except BitStringException as e:
        print(f"\nОшибка: {e}", file=sys.stderr)
        return 1

    input("\nНажмите Enter для выхода...")
    return 0


if __name__ == "__main__":
    sys.exit(main())
