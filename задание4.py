text = input("Введите строку: ")

#18 Найти в тексте даты формата «день.месяц.год».
import re
def find_dates(text):
    pattern = r'\b(\d{1,2}\.\d{1,2}\.\d{4})\b'
    dates = re.findall(pattern, text)
    return dates

if find_dates(text):
    for date in find_dates(text):
        print(date)
else:
    print("Формата «день.месяц.год» НЕТ.")
