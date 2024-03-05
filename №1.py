#Даны два списка чисел. Найдите все числа, которые входят как в первый,так и во второй список и выведите их в порядке возрастания.

list1 = input("Введите 1-й список: ").split()
list2 = input("Введите 2-й список: ").split()

list1 = list(map(int, list1))
list2 = list(map(int, list2))

common_nums = list(set(list1) & set(list2))

common_nums.sort()
print(common_nums)