# Напишите программу содержащую логическую функцию проверки списка чисел, на то составные ли они.
# Программа должна применять эту функцию к списку считанному с файла.

# false = составное,  true = простое

def prime(n):
    if n == 1 or n == 2:
        return False
    elif n > 2:
        for x in range(2, n):
            if n % x == 0:
                return False
    return True

a = []
f = open(input("Введите имя файла:"), "r")
for line in f:
    b = line.split()
    for n in b:
        n = int(n)
        a.append(prime(n))
print(a)
