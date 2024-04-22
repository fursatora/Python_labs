#!/usr/bin/env python3
import sqlite3
import cgi

print("Content-type: text/html\n")

# Получение данных из HTML-формы
form = cgi.FieldStorage()
name = form.getfirst("name")
email = form.getfirst("email")

# Создание подключения к базе данных
conn = sqlite3.connect('hotel.db')
c = conn.cursor()

sql='''\
INSERT INTO Guests (name, email) VALUES (?, ?)
'''
# Вставка данных в таблицу
c.executemany(sql,(name, email))

# Закрытие соединения с базой данных
conn.commit()
conn.close()

print("<html><head><meta http-equiv='refresh' content='0;URL=/guest_form.html'></head><body></body></html>")