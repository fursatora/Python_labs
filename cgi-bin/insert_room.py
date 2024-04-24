#!/usr/bin/env python3
import sqlite3
import cgi

print("Content-type: text/html; charset=UTF-8\n")

room_form = cgi.FieldStorage()
room_number = room_form.getfirst("room_number")
capacity=room_form.getfirst("capacity")
price=room_form.getfirst("price")

# Создание подключения к базе данных
conn = sqlite3.connect('cgi-bin/hotel.db')
c = conn.cursor()

sql_room='''\
INSERT INTO Rooms (room_number, capacity, price) VALUES (?, ?, ?)
'''
# Вставка данных в таблицу
c.execute(sql_room,(room_number, capacity, price))

# Закрытие соединения с базой данных
conn.commit()

print("<h1>Данные из базы данных:</h1>")
c.execute("SELECT * FROM Rooms")
rows = c.fetchall()

# Вывод данных в виде таблицы
print("<table>")
print("<tr><th>Номер комнаты</th><th>Вместимость</th><th>Цена за ночь</th></tr>")
for row in rows:
    print("<tr><td>{}</td><td>{}</td></tr>".format(row[1], row[2],row[3]))
print("</table>")
print("<a href='index.html'>На главную</a>")

conn.close()

#print("Location: /cgi-bin/show_info.py\n")