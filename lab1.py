#задание1 вар1
a=int (input("Введите число: "))

#найти сумму простых делителей числа
def sum_of_prime_factors(a):
    sum=0
    for i in range (2, a+1):
        k=0
        if  a%i==0:
            for j in range(2, i//2 + 1):
                if (i % j == 0):
                    k = k + 1
            if (k == 0):

                sum=sum+i
    sum=sum+1
    return sum
s=sum_of_prime_factors(a)
print ("Сумма простых делителей: ", s)


# найти кол-во нечётных цифр числа, больших 3
def number_of_odd_digits(a):
    k=0
    while a>0:
        if(a%2!=0 and a%10>3):
            k=k+1
        a=a//10
    return k
k=number_of_odd_digits(a)
print ("Kол-во нечётных цифр числа, больших 3: ",k)


#найти произведение таких делителей числа, сумма цифр которых меньше, чем сумма цифр исходного числа
def product_of_divisors(a):
    p=1
    sum1=0
    while a>0:
        sum1=sum1+a%10
        a=a//10

    for i in range (2, a+1):
        sum2=0
        if  a%i==0:
            while i > 0:
                sum2 = sum2 + a % 10
                i= i // 10
        if(sum2>sum1):
            print(p)
            p=p*i
    return p
p=product_of_divisors(a)
print ("Произведение таких делителей числа, сумма цифр которых меньше, чем сумма цифр исходного числа ",p)



#задание2 вар1
text = input("Введите строку: ")


#1 Дана строка. Необходимо найти общее количество русских символов.
def count_russian_characters(text):
        russian_chars = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        russian_chars += russian_chars.upper()

        count = 0
        for char in text:
            if char in russian_chars:
                count += 1
        return count
print("Количество русских символов в тексте:", count_russian_characters(text))


#9 Дана строка. Необходимо проверить образуют ли строчные символы латиницы палиндром.
def is_palindrome(s):
    s = ''.join([c.lower() for c in s if c.isalpha()])
    return s == s[::-1]
if is_palindrome(text):
    print("Палиндром.")
else:
    print("НЕ палиндром.")



