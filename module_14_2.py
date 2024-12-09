import sqlite3

# Создаем БД not_telegram.db
connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

# Удаляем таблицу Users, если она существует. Для того, чтобы таблица не разрасталась в случае
# нескольких запусков срипта подряд в процессе написания.
cursor.execute("DROP TABLE IF EXISTS Users")

# Создаем таблицу Users в БД not_telegram.db
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# Домашнее Задание. Часть 1 (предыдущее задание)
print('Домашнее Задание. Часть 1')
# Заполняем таблицу Users 10-ю записями согласно условию
for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f'User{i}', f'example{i}@gmail.com', i*10, 1000))

# Обновляем balance у каждой 2-ой записи начиная с 1-ой на 500
for i in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE id = ?",
                   (500, i))

# Удаляем каждую 3-ю запись в таблице начиная с 1-ой
for i in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE id = ?",
                   (i,))

# Получаем все записи, где возраст не равен 60
cursor.execute("SELECT * FROM Users WHERE age <> ?",
               (60,))
users = cursor.fetchall()

# Выводим полученные записи в консоль в заданном формате
for row in users:
    print(f"Имя:{row[1]} | Почта:{row[2]} | Возраст:{row[3]} | Баланс:{row[4]}")

# Домашнее Задание. Часть 2
print()
print('Домашнее Задание. Часть 2')
# Задача "Средний баланс пользователя"

cursor.execute("SELECT COUNT(username) FROM Users")
total_users0 = cursor.fetchone()[0]
print(f'Количество всех пользователей до удаления записи: {total_users0}')

# 1. Удалите из базы данных not_telegram.db запись с id = 6
cursor.execute("DELETE FROM Users WHERE id = ?",(6,))
print('Удаляем запись с id = 6')

# 2. Подсчитать общее количество записей
cursor.execute("SELECT COUNT(username) FROM Users")
total_users = cursor.fetchone()[0]
print(f'Количество всех пользователей: {total_users}')

# 3. Посчитать сумму всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]
print(f'Сумма всех балансов: {all_balances}')

# 4. Вывести в консоль средний баланс всех пользователей
print('Первый вариант среднего:', all_balances / total_users)
cursor.execute("SELECT AVG(balance) FROM Users")
avg_balances = cursor.fetchone()[0]
print(f'Второй вариант среднего: {avg_balances}')

connection.commit()
connection.close()
