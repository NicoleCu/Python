# код Хаффмана


from collections import Counter
from collections import namedtuple
import heapq


def base():
    a = input()   # ввод текста
    c = huffm(a)
    cc = []
    for i in a:
        cc.append(c[i])  # построение закодированной строки
    cc = ''.join(cc)
    print('Закодированное сообщение:', cc)
    for i in c:
        print(i, c[i])


class Node(namedtuple("Node", ["left", "right"])):  
        """"" Узел """""
        def run(self, c, p):
            self.left.run(c, p + "0")
            self.right.run(c, p + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    """"Листья дерева"""""
    def run(self, c, p):
        c[self.char] = p


def huffm(a):
    g = Counter(a)   # считает сколько раз символ встретился в строке
    h = []
    for i, t in g.items():
        h.append((t, len(h), Leaf(i)))
    heapq.heapify(h)   # преобразование списка h в кучу
    count = len(h)
    while len(h) > 1:
        t1, count1, left = heapq.heappop(h)   # минимальная частота
        t2, count2, right = heapq.heappop(h)   # следующий элемент с минимальной частотой
        heapq.heappush(h, (t1 + t2, count, Node(left, right)))  # добавление нового элемента , у которого частота равна сумме частот, в h
        count +=1
    [(t, count, root)] = h  # корень построенного дерева
    y = {}
    root.run(y, "")        # обход с корня и заполнение словаря, 2 аргумент - преффикс
    return y


base()    # вызов функции
