# Напишите программу, которая считывает текст состоящий одной строки и все слова
# с нечетным номером переводит в верхний регистр(заглавные буквы), а с четным - в нижний(прописные).

S = input('Введите текст:').split()
for i in range(len(S)):
    if i % 2 == 0:         # т.к. нумерация в массиве и строке различается на 1
        S[i] = S[i].upper()
    else:
        S[i] = S[i].lower()
for i in range(len(S)):
    S = ' '.join(S)
    break
print(S)