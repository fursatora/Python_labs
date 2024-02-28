#В порядке увеличения квадратичного отклонения между средним весом ASCII-кода символа в строке и максимально среднего ASCII-кода тройки подряд идущих символов в строке.
def average_weight(string):
    return sum(ord(char) for char in string) / len(string)

def max_weight(string):
    max_avg = 0
    for i in range(len(string) - 2):
        tri_avg = (ord(string[i]) + ord(string[i+1]) + ord(string[i+2])) / 3
        max_avg = max(max_avg, tri_avg)
    return max_avg


strings = []
n = int(input("Введите количество строк: "))
print("Введите строки:")
for _ in range(n):
    strings.append(input())

sorted_strings = sorted(strings, key=lambda x: ((average_weight(x) - max_weight(x))**2)**0.5)

print("Отсортированные строки:")
for string in sorted_strings:
    print(string)