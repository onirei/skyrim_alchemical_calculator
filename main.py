import sqlite3

# array = []
# n = 0
# #Блок чтения массива данных из текстового документа
# with open("skyrim.txt") as file:
# #    array = [row.strip() for row in file]  метод (list comprehension) пиздатый, но не вытащить по словам. https://ru.stackoverflow.com/questions/542210/%d0%a7%d1%82%d0%b5%d0%bd%d0%b8%d0%b5-%d0%b8%d0%b7-%d1%84%d0%b0%d0%b9%d0%bb%d0%b0-%d0%bf%d0%be%d1%81%d1%82%d1%80%d0%be%d1%87%d0%bd%d0%be-%d0%b8-%d0%b7%d0%b0%d0%bf%d0%b8%d1%81%d1%8c-%d0%b2-%d0%bc%d0%b0%d1%81%d1%81%d0%b8%d0%b2
#     for line in file.readlines():
#         j = ''
#         a = []
#         for i in line:
#             if i == '\t' or i == '\n':
#                 if i == '\t':
#                     j = j[0:-1]
#                 a.append(j)
#                 j = ''
#             else:
#                 j = j+i
#         array.append(a)
#         del (array[n][0])
#         n += 1
# print(array)

# Создаем соединение с нашей базой данных
# В нашем примере у нас это просто файл базы
# conn = sqlite3.connect('Skyrim.sqlite')
# # Создаем курсор - это специальный объект который делает запросы и получает их результаты
# cursor = conn.cursor()

# ТУТ БУДЕТ НАШ КОД РАБОТЫ С БАЗОЙ ДАННЫХ
# КОД ДАЛЬНЕЙШИХ ПРИМЕРОВ ВСТАВЛЯТЬ В ЭТО МЕСТО


# Делаем INSERT запрос к базе данных, используя обычный SQL-синтаксис
# sss = 'tasdvbn'
# cursor.execute("insert into atributs values (?)", [sss])
# Если мы не просто читаем, но и вносим изменения в базу данных - необходимо сохранить транзакцию
# conn.commit()
# Не забываем закрыть соединение с базой данных
# conn.close()



# conn = sqlite3.connect('Skyrim.sqlite')
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM atributs")
# result = cursor.fetchall()
# print(result)
# conn.close()

# conn = sqlite3.connect('Skyrim.sqlite')
# cursor = conn.cursor()
# try:
#     cursor.execute("""
#     CREATE TABLE Ingredients(
#        NAME           TEXT     NOT NULL,
#        ID             CHAR(8)  NOT NULL,
#        ATTRIBUTE_1    TEXT     NOT NULL,
#        ATTRIBUTE_2    TEXT     NOT NULL,
#        ATTRIBUTE_3    TEXT     NOT NULL,
#        ATTRIBUTE_4    TEXT     NOT NULL
#     )
#     """)
#     conn.commit()
# except Exception:
#     print('DB already exist')
# i = 0
# while i < len(array):
#     cursor.execute("insert into Ingredients values (?, ?, ?, ?, ?, ?)", [array[i][0], array[i][1], array[i][2], array[i][3], array[i][4], array[i][5]])
#     conn.commit()
#     i += 1
# conn.close()

# conn = sqlite3.connect('Skyrim.sqlite')
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM Ingredients")
# result = cursor.fetchall()
# print(result)
# conn.close()

conn = sqlite3.connect('Skyrim.sqlite')
cursor = conn.cursor()
cursor.execute("SELECT * FROM Ingredients")
result = cursor.fetchall()
i = 0
while i < len(result):
    print(result[i])
    i += 1
conn.close()

s1 = input('Введите первый параметр: ')
s2 = input('Введите второй параметр: ')
conn = sqlite3.connect('Skyrim.sqlite')
cursor = conn.cursor()
cursor.execute("""
SELECT *
  FROM Ingredients WHERE 
  (ATTRIBUTE_1 = (?)
  OR 
  ATTRIBUTE_2 = (?)
  OR 
  ATTRIBUTE_3 = (?)
  OR 
  ATTRIBUTE_4 = (?))
  AND
  (ATTRIBUTE_1 = (?)
  OR 
  ATTRIBUTE_2 = (?)
  OR 
  ATTRIBUTE_3 = (?)
  OR 
  ATTRIBUTE_4 = (?))
""", [s1, s1, s1, s1, s2, s2, s2, s2])
result = cursor.fetchall()
i = 0
while i < len(result):
    print(result[i])
    i += 1
conn.close()
