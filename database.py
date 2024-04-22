import sqlite3
import xml.dom.minidom

# Создаем XML-документ
doc = xml.dom.minidom.Document()
# Создаем корневой элемент
root = doc.createElement('table')
doc.appendChild(root)

# Подключение к базе данных
conn = sqlite3.connect('cgi-bin/hotel.db')
cursor = conn.cursor()

# Создание таблиц
cursor.execute('''
    CREATE TABLE IF NOT EXISTS rooms (
        room_number INTEGER PRIMARY KEY,
        capacity INTEGER,
        price REAL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS guests (
    guest_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS bookings (
    booking_id INTEGER PRIMARY KEY,
    guest_id INTEGER,
    room_number INTEGER,
    check_in_date DATE,
    check_out_date DATE,
    FOREIGN KEY (guest_id) REFERENCES guests(guest_id),
    FOREIGN KEY (room_number) REFERENCES rooms(room_number)
)
''')

# Закрытие соединения с базой данных
conn.commit()
conn.close()

print("Tables created successfully.")