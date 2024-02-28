#25 Дан целочисленный массив и интервал a..b. Необходимо найти максимальный из элементов в этом интервале.
def find_max(arr, a, b):
    interval = arr[a:b+1]
    return max(interval) if interval else None

arr = list(map(int, input("Массив: ").split()))
a, b = map(int, input("Интервал a...b: ").split())
max_in_interval = find_max(arr, a, b)

if max_in_interval is not None:
    print("Максимальный элемент", max_in_interval)
else:
    print("Интервал пуст или выходит за границы массива.")