# Реализуйте в виде рекурсивной функции алгоритм Быстрой Сортировки для массива чисел

import random
def f_sort(m):
    n = random.choice(m)
    if len(m) > 1:
        mx = [a for a in m if a > n]
        mn = [b for b in m if b < n]
        eq = [c for c in m if c == n]
        return mn + eq + mx

f = open(input("Введите имя файла:"), "r")
for line in f:
    m = line.split()
    print(f_sort(m))



