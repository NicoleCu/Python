# вычислить количество сочетаний из n по k

n = int(input("число n "))
k = input("число k ")
k = int(k)
fac1 = 1
fac2 = 1
i = 0
p = 0
y = 0
j = n - k
fac3 = 1
while i < n:
     i = i + 1
     fac1 = fac1 * i
while p < k:
     p = p + 1
     fac2 = fac2 * p
while y < j:
     y = y + 1
     fac3 = fac3 * y
print(fac1//(fac2*fac3))

