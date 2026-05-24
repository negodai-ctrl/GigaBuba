import sys
def input_bits():
    bits = ['0'] * 8
    s = input("Input bs: ")

    if len(s) > 8 or not all(c in '01' for c in s):
        print("Incorrect")
        sys.exit(0)

    for i, c in enumerate(s):
        bits[8 - len(s) + i] = c
    return bits

def file_input_bits(filename):
    try:
        with open(filename, 'r') as f:
            s = f.read().strip()
    except FileNotFoundError:
        print("File not found")
        sys.exit(0)

    bits = ['0'] * 8

    if len(s) > 8 or not all(c in '01' for c in s):
        print("Incorrect")
        sys.exit(0)

    for i, c in enumerate(s):
        bits[8 - len(s) + i] = c
    return bits


def output_bits(bits):
    print("Stroka =", ''.join(bits))


def ymn(bits1, bits2):
    return ['1' if b1 == '1' and b2 == '1' else '0' for b1, b2 in zip(bits1, bits2)]


def main():
    bs1 = ['0', '0', '0', '0', '0', '0', '0', '0']
    bs2 = ['0', '0', '0', '0', '0', '0', '0', '0']

    bs1 = file_input_bits("a.txt")
    bs2 = input_bits()

    print("BS 1:", end=' ')
    output_bits(bs1)
    print()
    print("BS 2:", end=' ')
    output_bits(bs2)
    print()

    res = ymn(bs1, bs2)
    output_bits(res)
    print(res)

if __name__ == "__main__":
    main()
    input("Press Enter to continue...")