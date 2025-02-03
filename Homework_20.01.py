# # Задача 1
# number = int(input("Введите число:"))
# i = 1
# while i**2 < number:
#     print(i**2)
#     i += 1

# Задача 2

# number = int(input("Введите число:"))
# while number // 10 != 0:
#     number = number // 10
#     print(number)




# Задача 3
# n = int(input('Введите число:'))
# min_digit = 9
# while n % 10 != 0:
#     n_2 = n % 10
#     print(n_2, 'Это число n_2 для сравнения с min_digit')
#     print(n, 'Это число n')
#     if n_2 < min_digit:
#         min_digit = n_2
#     print('Сейчас наименьшее число', min_digit)
#     n //= 10
# print(min_digit)

# Строки
#4
# string = input("Введите строку ")
# print(string)
# print(string[2])
# print(string[-2])
# print(string[0:5])
# print(string[:-2])
# print(string[0::2])
# print(string[1::2])
# print(string[5::-1])
# print(string[5::-2])
# print(len(string))
# #5
# string = 'привет андрей'
# print(len(string))
# print(string[7:],end=" ")
# print(string[0:6])
#
# string = ("a роза упала на лапу aзора".replace(" ",""))
# print(len(string))
# print(string)
# string_2 = string[27::-1]
# print(string_2 )
# lst_string = list(string)
# lst2_string = list(string_2)
# if lst_string.sort() == lst2_string.sort():
#     print(True)
# else: print(False)

# string = input("Введите строку:")
# x = string.count("f")
# y = string.find("f")
# if x == 1:
#     print(y)
# else:
#     print(x,y)


# #Задача 8
# lst_1 = [6, 4, 3, 7, 8]
# lst_2 = [3, 16, 7, 8, 2]
# a_lst_1  = lst_1[0]
# empty_list = list()
#
# for elem in lst_1:
#      if elem < a_lst_1:
#         a_lst_1 = elem
# if a_lst_1 in lst_2:
#     print(True)
#     empty_list1 = empty_list.append(lst_1.remove(a_lst_1))
#     print(lst_1)
#     a_lst_1 = lst_1[0]
#     for i in lst_1:
#         if i < a_lst_1:
#              a_lst_1 = i
#     print(a_lst_1)

# Задача 9

# number_list = [1,3,5,1,6,1,2,4,15,1]
# counter = 0
# for i in range(1, len(number_list)):
#     if number_list[i] > number_list[i - 1]:
#         counter += 0
#     if number_list[i] < number_list[i - 1]:
#         counter += 1
# print(counter)

# Задача 10
# string = input('Введите строку')
# first_let = []
# for i in string:
#     if i not in first_let:
#         first_let.append(i)
# print(''.join(first_let))
#

# Задача 11
# text = "dfsafasdfasdf 123123 asdffd 123"
# empty_list = []
#
# x=list(text.split( ))
# print(x)
# for i in x:
#     if i == int:
#         empty_list.append(i)
# print(empty_list)
