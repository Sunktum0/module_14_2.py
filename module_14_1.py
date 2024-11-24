import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Создание таблицы, если она не существует
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# Вставка данных, убедитесь, что эта строка не закомментирована
users = [
    ('User1', 'example1@gmail.com', 10, 1000),
    ('User2', 'example2@gmail.com', 20, 1000),
    ('User3', 'example3@gmail.com', 30, 1000),
    ('User4', 'example4@gmail.com', 40, 1000),
    ('User5', 'example5@gmail.com', 50, 1000),
    ('User6', 'example6@gmail.com', 60, 1000),
    ('User7', 'example7@gmail.com', 70, 1000),
    ('User8', 'example8@gmail.com', 80, 1000),
    ('User9', 'example9@gmail.com', 90, 1000),
    ('User10', 'example10@gmail.com', 100, 1000)
]

# # Используем executemany для вставки множества записей
# cursor.executemany("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", users)

# # # Обновление и удаление записей
# cursor.execute("UPDATE Users SET balance = balance - 500 WHERE id % 2 = 1")
# cursor.execute("DELETE FROM Users WHERE id % 3 = 1")
#
# # Выборка данных
# results = cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60").fetchall()


#  Вывод результатов
# for row in results:
#     print(f"Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}")

# удаление юзера с id 6
# cursor.execute("DELETE FROM Users WHERE id == 6")

cursor.execute("SELECT COUNT(*) FROM Users")
Total1 = cursor.fetchone() [0]
print(Total1)

cursor.execute("SELECT SUM(balance) FROM Users")
sum1 = cursor.fetchone()[0]
print(sum1)

cursor.execute("SELECT AVG(balance) FROM Users")
avg1 = cursor.fetchone()[0]
print(avg1)


# Подтверждение изменений и закрытие соединения
connection.commit()
connection.close()