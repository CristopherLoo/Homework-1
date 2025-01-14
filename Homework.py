import math as m
#привет марк
print("Hello,world")
print("Hi,mark")
print("lOVE YOU")

# Второе задание

age = 19
if age < 20:
    print("Мал да удал!")
if age >= 20:
    print("Нормалёк уголёк!")

# Третье задание

age = 1

if age <= 10:
    print("Красава")
elif age > 10 and age <= 25:
    print("норм")
else:
    print('Эх заживем')

# Четвертое задание

a = 7
b = 2
c = a % b
print(c)

a = 7
b = 2
c = a // b
print(c)

age = 1000
if age <= 25:
    print("маловат ты дядя")
elif age > 25 and age <= 35:
    print("взрословат ты дядя")
elif age >= 35 and age <= 45:
    print("здороват ты дядя")
elif age >= 45 and age <= 55:
    print("великоват ты дядя")
elif age >= 55 and age <= 75:
    print("староват ты дядя")
else:
    print("да ты еле на ногах стоишь!")

# Задача 1

x = 17 / 2 * 3 + 2
y = 2 + 17 / 2 * 3
c = 19 % 4 + 15 / 2 * 3
d = 15 + 6 - 10 * 4
f = 17 / 2 % 2 * 3 ** 3
print (x,y,c,d,f)

# Задача 2

x = 17 / 2 * (3 + 2)
y = (2 + 17) / 2 * 3
c = 19 % (4 + 15 )/ 2 * 3
d = (15 + 6 - 10) * 4
f = 17 / 2 % (2 * 3) ** 3
print (x,y,c,d,f)

# Задача 3

# Общее сумма денег
x = 11
# Стоимость одной буханки
y = 1.5
# Анна купила 3 буханки
c = y * 3
# Находим неизвестную
s = x - c
print (s)

x = 11
y = 1.5
c = x - y * 3
print(c)




# Общая сумма денег
x = 11
# Стоимость одной булочки
y = 1.5
# Анна купила 3 булочки
s = y * 3
# Находим неизвестную
c = x - s
print(c)  # Выводит оставшиеся деньги




# Задание 4
x = 2
y = 5
print("Пол:",y,"Анна:",x)

# Задание 5
f = 3
a = f * 24
b = a * 60
c = b * 60 * 60
print ("day:", f )
print("Sample Out:")
print(f,"cуток","=",a,"часов","=",b,"минут","=",c,"секунд")

height_ = 5
meter_up_per_day = 5
meter_down_per_day = 2
meter_per_day = meter_up_per_day - meter_down_per_day
count_of_day = height_ / meter_per_day
which_day = m.ceil(count_of_day)
if meter_up_per_day < meter_down_per_day:
    print("Число метров вверх должно быть больше чем низ,исправьте")
else:
    print("улитка приползёт на",which_day,"день")


