# Напишите программу вычисляющую минимум, максимум и среднее арифметическое элементов массива, введенного из консоли


i = int
z = float
n = int(input("Введите длину списка:"))
a = [0] * n
for i in range(n):
    a[i] = int(input("Введите элементы:"))
    mn = (a[0])
    mx = a[0]
    sm = 0
    for i in range(n):
        sm = sm + a[i]
    if a[i] < mn:
        mn = a[i]
    if a[i] > mx:
        mx = a[i]
        z = sm/n
        print('min:' + str(mn), 'max:' + str(mx), 'avg:' + str(z))
