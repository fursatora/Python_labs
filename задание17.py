#25 Дан целочисленный массив и интервал a..b. Необходимо найти максимальный из элементов в этом интервале.
arr = input("Введите ассив: ").split()
arr = [int(x) for x in arr]

a = int(input("Введите a: "))
b = int(input("Введите b: "))

if a > b or a < 0 or b >= len(arr):
    print("Некорректный интервал.")
else:
    subarray = arr[a:b + 1]
    max_element = max(subarray)
    print(f"Максимальный элемент в интервале: {max_element}")