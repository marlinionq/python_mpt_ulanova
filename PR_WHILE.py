
# 1. Выведите все числа от 1 до 10.
print("task 1")
i = 1
while i <= 10:
    print(i)
    i += 1

# 2. Вводите числа до 0. Найдите их сумму.
print("task 2")
n = int(input("Введите число: "))
sum = 0
while n != 0:
    sum += n
    n = int(input("Введите число: "))

print(sum)


# 3. Посчитайте количество цифр числа.
print("task 3")

n = int(input("Введите число: "))
count = 0

while n > 0:
    count += 1
    n //= 10

print(count)


# 4. Найдите сумму цифр числа.
print("task 4")

n = int(input("Введите число: "))
sum = 0

while n > 0:
    sum += n % 10
    n //= 10

print(sum)


# 5. Выведите число в обратном порядке.
print("task 5")

n = int(input("Введите число: "))
reverse = 0

while n > 0:
    reverse = reverse * 10 + n % 10
    n //= 10

print(reverse)


# 6. Выведите все степени двойки до n.
print("task 6")

n = int(input("Введите число: "))
i = 1

while i <= n:
    print(i)
    i *= 2


# 7. Запрашивайте пароль до правильного.
print("task 7")

password = input("Введите пароль: ")

while password != "123456":
    password = input("Неверный пароль. Попробуйте ещё: ")

print("Пароль правильный")


# 8. Найдите НОД двух чисел.
print("task 8")

x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))

while y != 0:
    ostatok = x % y
    x = y
    y = ostatok

print(x)


# 9. Выведите числа Фибоначчи до n.
print("task 9")

n = int(input("Введите число: "))
a = 0
b = 1

while a <= n:
    print(a)
    next_n = a + b
    a = b
    b = next_n


# 10. Игра "Угадай число".
print("task 10")

import random

n = random.randint(1, 100)
x = 0

while x != n:
    x = int(input("Угадайте число: "))

    if x < n:
        print("Больше")
    if x > n:
        print("Меньше")

print("Вы угадали!")
