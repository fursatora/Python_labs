text = input("Введите строку: ")

#1 Дана строка. Необходимо найти общее количество русских символов.
def count_russian_characters(text):
        russian_chars = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        russian_chars += russian_chars.upper()

        count = 0
        for char in text:
            if char in russian_chars:
                count += 1
        return count
print("Количество русских символов в тексте:", count_russian_characters(text))