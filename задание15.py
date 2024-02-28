#1 Дан целочисленный массив. Необходимо найти количество элементов,расположенных после последнего максимального.
arr = input("Введите массив: ").split()
arr = [int(x) for x in arr]

max_value = max(arr)
max_index = len(arr) - arr[::-1].index(max_value) - 1
count_after_max = len(arr) - max_index - 1

print("Количество элементов после последнего максимального:", count_after_max)