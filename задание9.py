#9 Прочитать список строк с клавиатуры. Упорядочить по длине строки.
n = int(input("Введите количество строк: "))
strings = []

for i in range(n):
    string = input(f"{i+1} ")
    strings.append(string)

sorted_strings = sorted(strings, key=len)
for string in sorted_strings:
    print(string)