#37 Дан целочисленный массив. Вывести индексы элементов, которые меньше своего левого соседа, и количество таких чисел.
arr = input("Введите массив: ").split()
arr = [int(x) for x in arr]

indexes = []

for i in range(1, len(arr)):
    if arr[i] < arr[i - 1]:
        indexes.append(i)
print("Индексы элементов, которые меньше своего левого соседа:", indexes)