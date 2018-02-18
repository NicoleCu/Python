# алгоритм шифрования RSA


import random
t = []
prime = []
w = []
z = []
for i in range(3, 100):              # генерация некоторого списка простых чисел
    for j in range(2, i, 2):            # Шаг = 2 для ускорения проверки простоты
        if i % j == 0:
            break
    else:
        prime.append(i)
p = random.choice(prime)      # выбираем 2 простых числа
q = random.choice(prime)
n = p*q
eu = (p - 1)*(q - 1)    # функция Эйлера от n
a = eu
for x in range(2, eu):                # поиск взаимно простых чисел и случайный выбор одного простого числа
    while a != 0 and x != 0:
        if a > x:
            a = a % x
        else:
            x = x % a
    if a + x:
        w.append(x)
for i in range(len(w)):
    l = 2
    while w[i] % l != 0:
        l += 1
    if l == w[i]:
        z.append(w[i])
e = random.choice(z)
print('Открытый ключ:', e, n)
for d in range(2, n+1):
    if (e*d) % n == 1:
        t.append(d)
d = random.choice(t)
print('Закрытый ключ:', d, n)
m = int(input('Сообщение:'))
c = (m**e) % n
print('Зашифрованное сообщение:', c)
f = int(input('Сообщение для расшифровки:'))
#расшифровка:
m1 = (f**d) % n
print('Исходное сообщение:', m1)