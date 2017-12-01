# Напишите программу, содержащую функцию вычисляющую функцию Эйлера для произвольного натурального числа.
# Программа должна считывать из файла массив чисел и находить среднее геометрическое значений функции
# Эйлера чисел массива.

import math
def euler(n):
    t = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            t = t + 1
    return t

a = []
k = 1
f = open(input(), "r")
for line in f:
    b = line.split()
    for n in b:
        n = int(n)
        a.append(euler(n))
x = len(a) - 1
while x != -1:
    k = a[x] * k
    x = x - 1
print(k**(1/len(b)))
