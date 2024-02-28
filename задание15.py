#1 Дан целочисленный массив. Необходимо найти количество элементов,расположенных после последнего максимального.
def elements_after_max(arr):
    if not arr:
        return 0

    max_val = max(arr)
    last_max_index = len(arr) - arr[::-1].index(max_val) - 1
    return len(arr) - last_max_index - 1

arr = list(map(int, input("Введите  массив: ").split()))

count = elements_after_max(arr)
print("Количество элементов после последнего максимального элемента:", count)