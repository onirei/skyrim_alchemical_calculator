import sqlite3
import os

array_all = []
array_pos = []
array_neg = []
array_1 = []
array_2 = []
potion = []

conn = sqlite3.connect('Skyrim.sqlite')
cursor = conn.cursor()
cursor.execute("SELECT * FROM Ingredients")
result = cursor.fetchall()
array_all = result
conn.close()

conn = sqlite3.connect('Skyrim.sqlite')
cursor = conn.cursor()
cursor.execute("SELECT * FROM Negative")
result = cursor.fetchall()
for i in range(0, len(result)):
    array_neg.append(result[i][0])
conn.close()

conn = sqlite3.connect('Skyrim.sqlite')
cursor = conn.cursor()
cursor.execute("SELECT * FROM Positive")
result = cursor.fetchall()
for i in range(0, len(result)):
    array_pos.append(result[i][0])
conn.close()


def foo(a, b):
    c = [a[0], a[1], b[0], b[1]]
    d = []
    e = []
    for k in range(2, len(a)):
        for l in range(2, len(b)):
            if all([(a[k] == b[l]), (a[k] in potion)]):
                d.append(a[k])
    for k in range(2, len(a)):
        if all([(a[k] in potion), (a[k] not in d), (a[k] not in e)]):
            e.append(a[k])
        if all([(b[k] in potion), (b[k] not in d), (b[k] not in e)]):
            e.append(b[k])
    bar(c, d, e)


def bar(a, b, c):
    for k in range(0, len(array_2)):
        d = []
        e = []
        for n in range(0, len(a)):
            d.append(a[n])
        for n in range(0, len(b)):
            e.append(b[n])
        check = False
        if array_2[k][2] in c:
            check = True
            e.append(array_2[k][2])
        elif array_2[k][3] in c:
            check = True
            e.append(array_2[k][3])
        elif array_2[k][4] in c:
            check = True
            e.append(array_2[k][4])
        elif array_2[k][5] in c:
            check = True
            e.append(array_2[k][5])
        if check:
            d.append(array_2[k][0])
            d.append(array_2[k][1])
            print(d)
            print(e)
            print()


def ingredients():
    for k in range(0, len(array_all)):
        print(array_all[k])


def properties():
    print('Положительные эффекты: ')
    for k in range(0, len(array_pos)):
        print(array_pos[k])
    print()
    print('Отрицательные эффекты: ')
    for k in range(0, len(array_neg)):
        print(array_neg[k])


def lib():
    checks = []
    print('Введите количество искомых свойств (1-4')
    s = input()
    if s == '1':
        s1 = input('dfghjk')
    elif s == '2':
        s1 = input()
        s2 = input()
    elif s == '3':
        s1 = input()
        s2 = input()
        s3 = input()
    elif s == '4':
        s1 = input()
        s2 = input()
        s3 = input()
        s4 = input()
    for k in range(0, len(array_all)):
        if s == '1':
            checks = [s1 in array_all[k]]
        elif s == '2':
            checks = [s1 in array_all[k], s2 in array_all[k]]
        elif s == '3':
            checks = [s1 in array_all[k], s2 in array_all[k], s3 in array_all[k]]
        elif s == '4':
            checks = [s1 in array_all[k], s2 in array_all[k], s3 in array_all[k], s4 in array_all[k]]
        if all(checks):
            print(array_all[k])


def optimizer():
    global potion
    s = input('Ключевой эффект: ')
    for k in range(0, len(array_all)):
        if s in array_all[k]:
            array_1.append(array_all[k])
        else:
            array_2.append(array_all[k])
        if s in array_pos[0:len(array_pos)]:
            potion = array_pos
        else:
            potion = array_neg
    k = 0
    l = 0
    while k < len(array_1) - 1:
        l += 1
        foo(array_1[k], array_1[l])
        if l == len(array_1) - 1:
            k += 1
            l = k


# for i in range(0, len(array_pos)):
#     if s in array_pos[i]:
#         potion = array_pos
# for i in range(0, len(array_neg)):
#     if s in array_neg[i]:
#         potion = array_neg

# for i in range(0, len(array_1)):
#     print(array_1[i])

while True:
    print('Ингредиенты Свойства Калькулятор Оптимизатор')
    mode = input('Выбирете действие: ')
    if mode == 'Ингредиенты':
        os.system('cls')
        ingredients()
    elif mode == 'Свойства':
        os.system('cls')
        properties()
    elif mode == 'Калькулятор':
        os.system('cls')
        lib()
    elif mode == 'Оптимизатор':
        os.system('cls')
        optimizer()
    else:
        os.system('cls')
        print('Неверная комманда')

# for i in range(0, len(array_2)):
#     print(array_2[i])
# for i in range(0, len(array_1)):
#     print(array_1[i])
# print(potion)
# for i in range(0, len(array)):
#     print(array[i])

# s1 = input('Введите ингридент: ')
# s2 = input('Введите ингридент: ')
#
# def lib():
#     for i in range(0, len(array)):
#         if all([(s1 in array[i]), (s2 in array[i])]):
#             print(array[i])
#     return True
