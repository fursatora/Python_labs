#13 Дан целочисленный массив. Необходимо разместить элементы, расположенные до минимального, в конце массива.
arr = input("Введите массив: ").split()
arr = [int(x) for x in arr]  # Преобразуем строки в целые числа

min_index = arr.index(min(arr))
before_min = arr[:min_index]
after_min = arr[min_index:]

new_arr = after_min + before_min

print("Массив после размещения элементов до минимального в конце:")
print(new_arr)