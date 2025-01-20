import math as m


# Задача 1

x = 17 / 2 * 3 + 2
y = 2 + 17 / 2 * 3
c = 19 % 4 + 15 / 2 * 3
d = 15 + 6 - 10 * 4
f = 17 / 2 % 2 * 3 ** 3
print(x, y, c, d, f)

# Задача 2

x = 17 / 2 * (3 + 2)
y = (2 + 17) / 2 * 3
c = 19 % (4 + 15) / 2 * 3
d = (15 + 6 - 10) * 4
f = 17 / 2 % (2 * 3) ** 3
print(x, y, c, d, f)

# Задача 3

# Общее сумма денег
x = 11
# Стоимость одной буханки
y = 1.5
# Анна купила 3 буханки
c = y * 3
# Находим неизвестную
s = x - c
print(s)

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
print("Пол:", y, "Анна:", x)

# Задание 5

f = 3
a = f * 24
b = a * 60
c = b * 60 * 60
print("day:", f)
print("Sample Out:")
print(f, "cуток", "=", a, "часов", "=", b, "минут", "=", c, "секунд")

# Задание 10

height_ = 111
meter_up_per_day = 2
meter_down_per_day = 41
meter_per_day = meter_up_per_day - meter_down_per_day
count_of_day = height_ / meter_per_day
which_day = m.ceil(count_of_day)
if meter_up_per_day < meter_down_per_day:
    print("Число метров вверх должно быть больше чем низ,исправьте")
else:
    print("улитка приползёт на", which_day, "день")

sec = 4213
min = sec // 60
hour = min // 60
ost_min = min - hour * 60
ost_sec = (sec - min * 60)
print(hour, "часа", ost_min, "минут",ost_sec,"секунд")

# Задание 7

# Высчитываем площадь первого прямоугольника

side_1 = 150
side_2 = 65
S_1 = side_1 * side_2

# Высчитываем площадь первого прямоугольника

side_3 = 30
side_4 = 30
S_2 = side_3 * side_4

# Делим одну площадь на другую

Count_sq = S_1 // S_2
print(Count_sq)

# Задание 9

cash = 364
# количество целых сотней
hundreds = cash // 100
fifty_bank = (cash - hundreds * 100) // 50
ten_bank = (cash - hundreds * 100 - fifty_bank * 50 ) // 10
unit_bank = cash - fifty_bank * 50 - hundreds * 100 - ten_bank * 10
print(hundreds,"банкноты по сто рублей,", fifty_bank,"банкноты по 50 рублей,", ten_bank,"банкнота по 10 рублей,", unit_bank,"банкноты по одному рублю,")

# Задание 8

hour = 1
S = 56
V = 45

t = 56 / 45
ost_t = t % hour
min = round(60 * ost_t)
hour = int(t - ost_t)
# Путь за который проедет байкер
print(hour, "час", min, "минут")
# Пусть время будет 1 ч 5 мин,переведем его в число
hour_2 = 1
ost_m_2 = 5
min_2 = (ost_m_2 / 60)
t_2 = min_2 + hour_2
S_2 = V * t_2
print(S_2,"километров")





