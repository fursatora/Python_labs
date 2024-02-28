#4 В порядке увеличения квадратичного отклонения среднего веса ASCII-кода символа строки от среднего веса ASCII-кода символа первой строки.
def average_weight(string):
    return sum(ord(char) for char in string) / len(string)

def quadratic_deviation_weight(string, avg_weight):
    return ((sum((ord(char) - avg_weight) ** 2 for char in string)) / len(string)) ** 0.5

strings = []
n = int(input("Кол-во строк: "))
print("Введите строки:")
for _ in range(n):
    strings.append(input())

first_avg_weight = average_weight(strings[0])
sorted_strings = sorted(strings, key=lambda x: quadratic_deviation_weight(x, first_avg_weight))

print("Отсортированные строки:")
for string in sorted_strings:
    print(string)