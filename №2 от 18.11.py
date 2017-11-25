# найти количество взаимно простых с n чисел, не превосходящих квадрат n

n = int(input("Ведите число: "))
b = []
t = n*n
k = 0
if n < 0:
    n = - n
for i in range(2, n + 1):
    if n % i == 0:
        b.append(i)
while t != 0:
    for i in b:
        if t % i != 0:
            k = k + 1
            t = t - 1
        else:
            t = t - 1
for f in range(1):
    print("Количество:" + str(k)) 

