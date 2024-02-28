#В порядке увеличения среднего количества «зеркальных» троек (например, «ada») символов в строке.
def count_mirror(string):
    count = 0
    for i in range(len(string) - 2):
        if string[i:i+3] == string[i:i+3][::-1]:
            count += 1
    return count

def sort_by_mirror(strings):
    return sorted(strings, key=lambda x: count_mirror(x))

strings = []
n = int(input("Кол-во строк: "))
print("Введите строки:")
for _ in range(n):
    strings.append(input())

sorted_strings = sort_by_mirror(strings)

for string in sorted_strings:
    print(string)