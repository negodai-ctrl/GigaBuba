bs1 = input('Input bs 1: ')
if len(bs1) > 8:
    print("Incorrect input")
    exit()
for b in bs1:
    if (b != "0") and (b != '1'):
        print("Incorrect input")
        exit()

d = 8 - len(bs1)
suffix = '0' * d
bs1 = suffix + bs1

bs2 = input('Input bs 2: ')
if len(bs2) > 8:
    print("Incorrect input")
    exit()
for b in bs2:
    if (b != "0") and (b != '1'):
        print("Incorrect input")
        exit()

d = 8 - len(bs2)
suffix = '0' * d
bs2 = suffix + bs2

bs3 = ""
i = 0
while i < 8:
    if bs1[i] == '1' and bs2[i] == '1':
        bs3 += '1'
    else:
        bs3 += '0'
    i += 1
print('Result=', bs3)