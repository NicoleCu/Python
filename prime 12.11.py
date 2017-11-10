# Напишите программу, которая находит во входном потоке простые числа. Входной поток заканчивается символом ‘!’

a = str
while a != "!":
    a = input("Ввод:")
    if a.isdigit():
        c = int(a)
        if c == 1:
            print(str(a) + ':единица')
        if c >= 2:
            for x in range(2, c):
                if c % x == 0:
                    print(str(a) + ':составное')
                break

            else:
                print(str(a) + ':простое')
    else:
        print(str(a) + ":не число")


