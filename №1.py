import math
class Pentagon:
    def __init__(self, identif, a, x, y):
        self.identif = identif
        self.a = a
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x
        if not isinstance(x, (int, float)):
            raise Exception("Введенные данные не являются числом")

    def set_y(self, y):
        self.y = y
        if not isinstance(y, (int, float)):
            raise Exception("Введенные данные не являются числом")
    def set_a(self, a):
        self.a = a
        if a < 0:
            raise Exception("Длина стороны меньше нуля")
        if not isinstance(a, (int, float)):
            raise Exception("Введенные данные не являются числом")

    def coord(self):
        pentagonCoord = [(self.x, self.y), (self.x + self.a, self.y), (self.x + self.a * math.cos(2*math.pi/5), self.y - self.a * math.sin(2*math.pi/5)), (self.x + self.a * math.cos(math.pi/5), self.y - self.a * math.sin(math.pi/5)), (self.x - self.a * math.cos(math.pi/5), self.y - self.a * math.sin(math.pi/5))]
        return pentagonCoord

    def to_string(self):
        print("Пятиугольник", self.identif, "с координатами x =", self.x, "y =", self.y, "и стороной равной", self.a)

    def is_include(self, rectangle):
        rectangle_coords = rectangle.coord()
        for x, y in rectangle_coords:
            if not (self.x <= x <= self.x + self.a and
                    self.y - self.a * math.sin(math.pi / 5) <= y <= self.y):
                return False
        return True

    def area(self):
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.a ** 2




class Rectangle:
    def __init__(self, identif, a,b, x, y):
        self.identif = identif
        self.a = a
        self.b = b
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x
        if not isinstance(x, (int, float)):
            raise Exception("Введенные данные не являются числом")

    def set_y(self, y):
        self.y = y
        if not isinstance(y, (int, float)):
            raise Exception("Введенные данные не являются числом")
    def set_a(self, a):
        self.a = a
        if a < 0:
            raise Exception("Ширина  меньше нуля")
        if not isinstance(a, (int, float)):
            raise Exception("Введенные данные не являются числом")

    def set_b(self, b):
        self.height = b
        if b < 0:
            raise Exception("Высота меньше нуля")
        if not isinstance(b, (int, float)):
            raise Exception("Введенные данные не являются числом")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def coord(self):
        rectangleCoord = [(self.x, self.y), (self.x + self.a, self.y), (self.x + self.a, self.y - self.b), (self.x, self.y - self.b)]
        return rectangleCoord

    def to_string(self):
        print("Прямоугольник", self.identif, "с координатами x =", self.x, "y =", self.y, ", шириной", self.a,
              "и высотой", self.b)

    def is_include(self, pentagon):
        pentagon_coords = pentagon.coord()
        for x, y in pentagon_coords:
            if not (self.x <= x <= self.x + self.a and
                    self.y - self.b <= y <= self.y):
                return False
        return True

    def area(self):
        return self.a * self.b

def compare(obj1, obj2):
    area1 = obj1.area()
    area2 = obj2.area()
    if area1 > area2:
        return 'Площадь первой фигуры больше'
    elif area1 < area2:
        return 'Площадь второй фигуры больше'
    else:
        return 'Площади равны'



rectangle = Rectangle("001", 1, 2, -2, 1)
pentagon = Pentagon("002",5, -2, 1)
rectangle.to_string()
pentagon.to_string()
print("Включена ли 1-я фигура во 2-ю: ", rectangle.is_include(pentagon))
print("Включена ли 2-я фигура во 1-ю: ", pentagon.is_include(rectangle))

rectangle.set_x(2)
rectangle.set_y(2)
rectangle.set_a(4)
pentagon.set_x(4)
pentagon.set_y(4)
pentagon.set_a(4)
rectangle.to_string()
pentagon.to_string()

print("Сравнение площадей: ", compare(rectangle, pentagon))

rectangle.set_x("абв")
