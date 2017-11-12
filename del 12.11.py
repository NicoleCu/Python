# Напишите программу, которая удаляет из массива все простые числа встречающиеся больше одного раза.

n = int(input('Введите длину списка:'))
a = [0] * n
b = list()
for i in range(n):
    a[i] = int(input('Введите числа:'))
    if a[i] < 2:
        b.append(a[i])
    else:
        for x in range(2, a[i]):
            if a[i] % x == 0:
                b.append(a[i])
        for x in range(2, a[i]):
            if a[i] % x != 0:
                v = a[i]
                c = i
                for p in range(c, n):
                    if a[p] != v:
                        b.append(a[p])
            break
for i in range(n):
    print(b)
    break