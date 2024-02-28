#37 Дан целочисленный массив. Вывести индексы элементов, которые меньше своего левого соседа, и количество таких чисел.
numbers = input("Введите массив: ").split()
numbers = [int(x) for x in numbers]

indexes = []

for i in range(1, len(numbers)):
    if numbers[i] < numbers[i - 1]:
        indexes.append(i) 
print("Индексы элементов, которые меньше своего левого соседа:", indexes)