# 1. Выведите все числа от 1 до 10.
print ("task 1")
for i in range (1,11):
    print (i) 
# 2. Выведите все чётные числа от 2 до 50.
print ("task 2")
for i in range (2,51,2):
    print (i)
# 3. Выведите числа от 10 до 1 в порядке убывания.
print ("task 3")
for i in range (10,0,-1):
    print (i)
# 4. Дано число n. Найдите сумму всех чисел от 1 до n.
print ("task 4")
n = int(input("Введите число: "))
sum = 0
for i in range (1,n+1):
    sum += i
print (sum)
# 5. Дано число n. Найдите его факториал.
print ("task 5")
n = int(input("Введите число: "))
work = 1
for i in range (1,n+1):
    work *= i
print (work)
# 6. Дано число n. Выведите таблицу умножения на n от 1 до 10.
print ("task 6")
n = int(input("Введите число: "))
for i in range (1,11):
    print(n*i)
# 7. Дан список чисел. Посчитайте, сколько в нём положительных чисел.
print ("task 7")
list = [-1, 7, 5, -8]
sum = 0
for i in list:
    if i>0:
        sum += 1
print (sum)

# 8. Дана строка. Посчитайте, сколько в ней гласных букв.
print ("task 8")
word = str(input("Введите слово: "))
sum = 0
for i in word:
    if i in "ёуеыаоэяию":
        sum += 1
print (sum)

# 9. Дан список чисел. Найдите наибольший элемент, не используя max().
print ("task 9")
x = [2,7,10,6,1]
biggest = x[0]
for i in x:
    if i > biggest:
        biggest = i
print (biggest)
# 10. Выведите таблицу умножения от 1 до 9 в виде квадрата
print ("task 10")
for i in range (1,10):
    for o in range (1,10):
        print (i*o, end="\t")
    print()
