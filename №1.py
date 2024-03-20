import re

def is_valid_phone_number(phone_number):
    pattern = r'^\+?[0-9]{1,3}\s?[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$'
    if re.match(pattern, phone_number):
        return True
    return False

def validate_phone_number(phone_number):
    if not is_valid_phone_number(phone_number):
        raise ValueError("Некорректный номер телефона")

    return phone_number

ex_phone_number = "+1 (555) 123-4567"
if is_valid_phone_number(ex_phone_number):
    print(f"{ex_phone_number} - корректный номер телефона")
else:
    print(f"{ex_phone_number} - некорректный номер телефона")
try:
    phone = validate_phone_number("+79788214859")
    print(f"Проверка прошла успешно: {phone}")
except ValueError as e:
    print(f"Ошибка: {e}")