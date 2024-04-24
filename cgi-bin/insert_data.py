#!/usr/bin/env python3
import sqlite3
import cgi

print("Content-type: text/html; charset=UTF-8\n")

# Получение данных из HTML-формы
guest_form = cgi.FieldStorage()
name = guest_form.getfirst("name")
email = guest_form.getfirst("email")


# Создание подключения к базе данных
conn = sqlite3.connect('cgi-bin/hotel.db')
c = conn.cursor()

sql_guest='''\
INSERT INTO Guests (name, email) VALUES (?, ?)
'''

# Вставка данных в таблицу
c.execute(sql_guest,(name, email))

# Закрытие соединения с базой данных
conn.commit()

print("<h1>Данные из базы данных:</h1>")
c.execute("SELECT * FROM Guests")
rows = c.fetchall()

# Вывод данных в виде таблицы
print("<table>")
print("<tr><th>Имя</th><th>Email</th></tr>")
for row in rows:
    print("<tr><td>{}</td><td>{}</td></tr>".format(row[1], row[2]))
print("</table>")

conn.close()

