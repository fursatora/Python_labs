#!/usr/bin/env python3
import sqlite3
import cgi

# Получение данных из формы
form = cgi.FieldStorage()
guest_id = form.getvalue('guest_id')
room_number = form.getvalue('room_number')
check_in_date = form.getvalue('check_in_date')
check_out_date = form.getvalue('check_out_date')

# Подключение к базе данных
conn = sqlite3.connect('cgi-bin/hotel.db')
c = conn.cursor()

# Вставка данных в таблицу bookings
c.execute("INSERT INTO bookings (guest_id, room_number, check_in_date, check_out_date) VALUES (?, ?, ?, ?)",
          (guest_id, room_number, check_in_date, check_out_date))
conn.commit()
conn.close()

# Перенаправление на страницу подтверждения (или другую страницу)
print("Status: 302 Found")
print("Location: /cgi-bin/confirmation.py\n")  # Замените на вашу страницу подтверждения
print("")