def count_nums(arr, n, k):
    arr.sort()

    max1 = arr[-1]
    max2 = arr[-2]
    max3 = arr[-3]

    for i in range(n - 4, -1, -1):
        if (max1 - arr[i] >= k) and (max2 - arr[i] >= k):
            if arr[i] > max3:
                max3 = arr[i]
            if max3 > max2:
                max2, max3 = max3, max2
            if max2 > max1:
                max1, max2 = max2, max1

    return max1, max2, max3



with open('a27_168.txt', 'r') as file:
    N_a, K_a = map(int, file.readline().split())
    nums_a = [int(line.strip()) for line in file]


with open('b27_168.txt', 'r') as file:
    N_b, K_b = map(int, file.readline().split())
    nums_b = [int(line.strip()) for line in file]

resultA = count_nums(nums_a,N_a, K_a)
resultB = count_nums(nums_b,N_b, K_b)

print("Для файла А:", resultA)
print("Максимальное произведение чисел:", (resultA[0] * resultA[1] * resultA[2])%(10**6+1))
print("Для файла B:", resultB)
print("Максимальное произведение чисел:", (resultB[0] * resultB[1] * resultB[2])%(10**6+1))