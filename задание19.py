#49 Для введенного списка положительных чисел построить список всех положительных простых делителей элементов списка без повторений.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_factors(numbers):
    prime_factors_set = set()
    for num in numbers:
        if num <= 1:
            continue
        for i in range(2, num + 1):
            if num % i == 0 and is_prime(i):
                prime_factors_set.add(i)
    return sorted(list(prime_factors_set))


numbers = input("Введите список положительных чисел: ").split()
numbers = [int(x) for x in numbers if x.isdigit() and int(x) > 0]
result = prime_factors(numbers)
print("Положительные простые делители элементов списка без повторений:", result)