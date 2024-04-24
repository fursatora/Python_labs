#!/usr/bin/env python3
import sqlite3
import cgi
from jinja2 import Environment, FileSystemLoader

# Подключение к базе данных
conn = sqlite3.connect('cgi-bin/hotel.db')  # Укажите путь к вашей базе данных
c = conn.cursor()

# Получение данных для выпадающих списков
c.execute("SELECT name FROM Guests")
guests = c.fetchall()
c.execute("SELECT room_number FROM Rooms")
rooms = c.fetchall()
conn.close()

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('booking_form.html')
html_form = template.render(guests=guests, rooms=rooms)

print("Content-type: text/html\n")
print(html_form)