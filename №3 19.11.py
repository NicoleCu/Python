# Напишите программу, которая обрабатывает файлы с результатами секвенирования.
# В первой строке файла лежит количество цепочек и другая вспомогательная информация.
# В остальных строчках - последовательности нуклеотидов. Если файл корректный - нужно вывести в консоль информацию
# о том, что секвенировалось(DNA/RNA) и информацию  количестве нуклеотидов каждого типа.
# А если файл отсутствует или некорректный - информацию что не так.

k = 0
u = 0
a = 0
c = 0
g = 0
y = []
try:
    f = open(input("file:"), "r")
except FileNotFoundError:
    print('file does not exist')
else:
    lines = f.readlines()
    lines = ''.join(lines[1:])
    b = list(lines)
    for i in range(len(b)):
        b[i] = b[i].lower()
        y.append(b[i])
    if 'u' in y and 't' in y:
        print('not correct: thymine and uracil can`t be together')
    elif 'u' in y:
        for i in range(len(y)):
            if y[i] == 'a':
                a = a + 1
            elif y[i] == 'c':
                c = c + 1
            elif y[i] == 'g':
                g = g + 1
            elif y[i] == 'u':
                u = u + 1
        print('RNA', "A:" + str(a), "U:" + str(u), "G:" + str(g), "C:" + str(c), sep='\n')
    else:
        for i in range(len(y)):
            if y[i] == 't':
                k = k + 1
            elif y[i] == 'a':
                a = a + 1
            elif y[i] == 'c':
                c = c + 1
            elif y[i] == 'g':
                g = g + 1
        print("DNA", "A:" + str(a), "T:" + str(k), "G:" + str(g), "C:" + str(c), sep='\n')