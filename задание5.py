#Дана строка. Необходимо найти все даты, которые описаны в "31 февраля 2007".

import re
text = input("Введите строку: ")
pattern = r'\b(\d{1,2} [а-я]+\s\d{4})\b'
dates = re.findall(pattern, text, flags=re.IGNORECASE)
print("Даты в нужном формате:")
for date in dates:
    print(date)