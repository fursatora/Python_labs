#!/usr/bin/env python
import sqlite3
import cgi

# Создание подключения к базе данных
conn = sqlite3.connect('cgi-bin/hotel.db')
c = conn.cursor()

# Выполнение SQL-запроса для получения данных
c.execute("SELECT * FROM Rooms")
rooms = c.fetchall()

c.execute("SELECT * FROM Guests")
guests = c.fetchall()

# Получение данных из HTML-формы
form = cgi.FieldStorage()
name = form.getfirst("name")
email = form.getfirst("email")


for room in rooms:
  print(room)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
<html>
<head>
<meta charset="cp1251">
<title>Информация об отеле </title>
    </head>
    <body>""")
print("<h1>Rooms</h1>")
print("<ul>")
for room in rooms:
    print("<li>Room number:", room[0], "</li>")
    print("<li>Capacity:", room[1], "</li>")
    print("<li>Price:", room[2], "</li>")
    print("<br>")
print("</ul>")
print("""</body> </html>""")

# Закрытие соединения с базой данных
conn.close()