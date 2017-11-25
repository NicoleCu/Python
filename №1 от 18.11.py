# вывести 2*k число последовательности Фибоначчи

k = int(input())
n = 2*k
f1 = 0
f2 = 1
i = 2
while i < n:
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    i = i + 1
print(f3)


