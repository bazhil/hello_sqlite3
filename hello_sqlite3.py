import sqlite3

# Знакомство с sqlite3 по статье https://habr.com/ru/post/321510/

conn = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()

# Чтение данных из базы
try:
    cursor.execute("SELECT Name FROM Artist ORDER BY Name")
    results = cursor.fetchall()
    print(results)
except sqlite3.DatabaseError as err:
    print('Error: ', err)
else:
    conn.commit()

# Запись данных в базу
try:
    cursor.execute("insert into Artist values (Null, 'ILWT') ")
    conn.commit()
    cursor.execute("""
        SELECT *
        FROM Artist
        WHERE name LIKE 'I%'""")

    results = cursor.fetchall()
    print(results)
except sqlite3.DatabaseError as err:
    print('Error: ', err)
else:
    conn.commit()

#  Подстановка значения в запрос
try:
    cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT ?", ('4'))
    results = cursor.fetchall()
    print(results)

    cursor.execute("SELECT Name from Artist ORDER BY Name LIMIT :limit", {"limit": 5})
    results = cursor.fetchall()
    print(results)
except sqlite3.DatabaseError as err:
    print('Error: ', err)
else:
    conn.commit()

# Получаем результаты по одному
try:
    cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
except sqlite3.DatabaseError as err:
    print('Error: ', err)
else:
    conn.commit()

conn.close()