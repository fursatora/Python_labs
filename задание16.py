#13 Дан целочисленный массив. Необходимо разместить элементы, расположенные до минимального, в конце массива.
def move_elements(arr):
    if not arr:
        return arr

    min_val = min(arr)
    min_index = arr.index(min_val)
    return arr[:min_index] + arr[min_index + 1:] + [min_val]

arr = list(map(int, input("Введите массив: ").split()))
modified_arr = move_elements(arr)

print("Массив после перемещения:")
print(modified_arr)