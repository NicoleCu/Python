# Напишите программу, которая обрабатывает файл “1-in.txt” с результатами сессии студентов.
# В файле в первой строке лежит число студентов, количество зачетов и экзаменов.
# Затем про каждого студента: ФИО, результаты зачетов(зачтено/незачтено) и оценки за экзамены.
# Программа должна в файл “1-out.txt" записать информацию про каждую категорию  студентов:
# стипендианты(все сдано с оценками не ниже 4),
# отчисленные(более двух предметов не сдано), должники(что-то не сдано, но не больше 2-х долгов), остальные.
# Выходной файл должен состоять из 8 строк: 1 строка) Стипендианты: количество, 2 строка) Фамилии стипендиантов...

z = []
r = 0
u = []
q = []
k = 0
i = 0
y = 0
ost = []
f = open("1-in.txt", "r", encoding="latin_1")
for line in f:
    b = line.split()
    for o in range(len(b)):
        if b[o] == "2":
            y = y + 1
        if b[o] == "don`t":
            y = y + 1
            if y > 2:
                i = i + 1
                z.append(b[0])
            elif y == 2 or y == 1:
                r = r + 1
                q.append(b[0])
            elif y == 0 and "3" in b:
                ost.append(b[0])
ouf = open("1-out.txt", "w")
ouf.write("отчисленные:" + str(i) + '\n')
ouf.write(' '.join(z) + '\n')

f = open("1-in.txt", "r", encoding="latin_1")
for line in f:
    b = line.split()
    if not "2" in b and not "3" in b and not "don`t" in b:
        k = k + 1
        u.append(b[0])
ouf = open("1-out.txt", "a")
ouf.write("стипендианты:" + str(k) + '\n')
ouf.write(''.join(u) + '\n')
f = open("1-in.txt", "r", encoding="latin_1")
ouf = open("1-out.txt", "a")
m = list(f)
ouf.write("остальные:" + str(len(m) - (k + i + r + 1)) + '\n')
ouf.write(''.join(ost)+'\n')
ouf.write("должники:" + str(r) + '\n')
ouf.write(''.join(q))
f.close()
ouf.close()
