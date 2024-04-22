import sqlite3

# Создание подключения к базе данных
conn = sqlite3.connect('hotel.db')
c = conn.cursor()

# Заполнение таблиц начальными данными
c.execute("INSERT INTO Rooms (room_number, capacity, price) VALUES (101, 1, 100.00)")
c.execute("INSERT INTO Rooms (room_number, capacity, price) VALUES (102, 1, 150.00)")
c.execute("INSERT INTO Rooms (room_number, capacity, price) VALUES (103, 2, 100.00)")
c.execute("INSERT INTO Rooms (room_number, capacity, price) VALUES (104, 3, 170.00)")
c.execute("INSERT INTO Rooms (room_number, capacity, price) VALUES (105, 4, 200.00)")

c.execute("INSERT INTO Guests (name, email) VALUES ('John Doe', 'john@example.com')")
c.execute("INSERT INTO Guests (name, email) VALUES ('Jane Smith', 'jane@example.com')")
c.execute("INSERT INTO Guests (name, email) VALUES ('Clare Ray', 'clare@example.com')")
c.execute("INSERT INTO Guests (name, email) VALUES ('Ann Polson', 'ann@example.com')")

# Закрытие соединения с базой данных
conn.commit()
conn.close()