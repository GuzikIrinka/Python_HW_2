# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

num = input()
sum = 0

for i in str(num):
    if i != ".":
        sum += int(i)
print(sum)


# Напишите программу, которая принимает на вход число N и выдает
# набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# from math import factorial

N = int(input('Введите число: '))
factorial = 1
for i in range(1, N+1):
    factorial *= i
print(factorial)


#Задайте список из n чисел последовательности (1+1/n)**n
# и выведите на экран их сумму.

n = int(input('Введите число: '))
sum = 0
for i in range (1, n+1):
    sum += (1 + 1/i)**i
print(sum) 


#Реализуйте алгоритм перемешивания списка.

import random
l=[9,8,7,6,5,4,3,2,1]
random.shuffle(l)
print(l)
