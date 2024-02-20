# Дан список строк с клавиатуры. Упорядочить по количеству слов в строке.

n = int(input("Введите количество строк: "))
strings = []

for i in range(n):
    string = input(f"Введите строку {i+1}: ")
    strings.append(string)

sorted_strings = sorted(strings, key=lambda x: len(x.split()))
for string in sorted_strings:
    print(string)