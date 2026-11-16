# 1. Создайте словарь из трёх учеников и их оценок. Выведите оценку одного
# ученика по его имени.
print("task 1")

students = {"Masha": 5, "Sasha": 4, "Glasha": 3}

print(students["Masha"])

# 2. Дан словарь. Добавьте в него новую пару, измените значение одного из
# ключей, удалите другой ключ и выведите результат.
print("task 2")

students = {"Masha": 5, "Sasha": 4, "Glasha": 3}
students["Dasha"] = 4
students["Glasha"] = 5
del students["Sasha"]

print(students)

# 3. Дан словарь и ключ. Выведите значение по этому ключу, а если такого
# ключа нет, выведите «Нет такого ключа».
print("task 3")

students = {"Masha": 5, "Sasha": 4, "Glasha": 3}

name = input("Введите имя: ")

if name in students:
    print(students[name])
else:
    print("Нет такого имени")
    
# 4. Дан словарь. Выведите отдельно все его ключи, все значения и количество
# пар.
print("task 4")

students = {"Masha": 5, "Sasha": 4, "Glasha": 3}

print(students.keys())
print(students.values())
print(len(students))

# 5. Дан словарь товаров и их цен. Выведите каждый товар и его цену с новой
# строки.
print("task 5")

groceries = {"Milk": 90, "Apple": 20, "Bread": 50}

for i in groceries:
    print(i, groceries [i])

# 6. Дан словарь товаров и их цен. Найдите сумму всех цен и название самого
# дорогого товара.
print("task 6")

groceries = {"Milk": 90, "Apple": 20, "Bread": 50}
sum = 0
for i in groceries:
    sum += groceries [i]
print ("Сумма: ", sum)
biggest = 1
for i in groceries:
    if groceries [i] > biggest:
            biggest = groceries [i]
            name = i
print (name)

# 7. Дана строка. Посчитайте, сколько раз в ней встречается каждый символ, и
# сохраните результат в словарь.
print("task 7")
str = "обороноспособность"
sumbols = {}

for i in str:
    if i in sumbols:
          sumbols [i] += 1
    else: 
        sumbols[i] = 1    
     
print (sumbols)

# 8. Дана строка из слов через пробел. Посчитайте, сколько раз встречается
# каждое слово, и выведите самое частое.
print("task 8")
str2 = "корабли лавировали лавировали да да да нет" 
words = {}

for i in str2.split():
    if i in words:
        words [i] += 1
    else:
        words [i] = 1
print (words)
biggest = 0
for i in words:
    if words [i] > biggest:
          biggest = words [i]
          word = i 
print (word)
     
# 9. Дан словарь. Создайте новый словарь, в котором ключи и значения
# поменяны местами.
print("task 9")

groceries = {"Milk": 90, "Apple": 20, "Bread": 50}
new_groceries = {}

for i in groceries:
     new_groceries [groceries[i]] = i 

print (new_groceries)

# 10. Даны два списка одинаковой длины: страны и их столицы. Составьте из
# них словарь и выведите столицу страны, которую введёт пользователь.
print("task 10")

countries = ["Russia", "Italy", "France", "China"]
capitals = ["Moscow", "Roma", "Paris", "Beijing"]
pairs = {}
for i in range (len(countries)):
     pairs [countries[i]] = capitals[i]

a = input ("Введите страну: ")
if a in pairs:
    print (pairs[a])
else:
     print ("Такой страны нет в списке")

