#!/usr/bin/env python
import sqlite3
import cgi

# Подключение к базе данных
conn = sqlite3.connect('hotel.db')
cursor = conn.cursor()

# Создание HTML-заголовка
print("Content-type: text/html\n")

# Получение данных из таблицы и формирование HTML-кода
cursor.execute('SELECT * FROM rooms')
rooms_data = cursor.fetchall()

cursor.execute('SELECT * FROM guests')
guests_data = cursor.fetchall()

cursor.execute('SELECT * FROM bookings')
bookings_data = cursor.fetchall()

# Вывод HTML-страницы с данными
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hotel Database</title>
</head>
<body>
    <h1>Rooms</h1>
    <table border="1">
        <tr>
            <th>Room Number</th>
            <th>Capacity</th>
            <th>Price</th>
        </tr>
""")
for room in rooms_data:
    print(f"""
        <tr>
            <td>{room[0]}</td>
            <td>{room[1]}</td>
            <td>{room[2]}</td>
        </tr>
    """)
print("""
    </table>

    <h1>Guests</h1>
    <table border="1">
        <tr>
            <th>Guest ID</th>
            <th>Name</th>
            <th>Email</th>
        </tr>
""")
for guest in guests_data:
    print(f"""
        <tr>
            <td>{guest[0]}</td>
            <td>{guest[1]}</td>
            <td>{guest[2]}</td>
        </tr>
    """)
print("""
    </table>

    <h1>Bookings</h1>
    <table border="1">
        <tr>
            <th>Booking ID</th>
            <th>Guest ID</th>
            <th>Room Number</th>
            <th>Check-in Date</th>
            <th>Check-out Date</th>
        </tr>
""")
for booking in bookings_data:
    print(f"""
        <tr>
            <td>{booking[0]}</td>
            <td>{booking[1]}</td>
            <td>{booking[2]}</td>
            <td>{booking[3]}</td>
            <td>{booking[4]}</td>
        </tr>
    """)
print("""
    </table>
</body>
</html>
""")

# Закрытие соединения с базой данных
conn.close()