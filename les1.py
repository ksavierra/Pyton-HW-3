# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list = list(map(int, input("Введите числа через пробел:\n").split()))

def sumOddIndex(list):
    sum = 0
    for i in range(len(list)):
        if i % 2 != 0:
            sum += list[i]
    print(f"Сумма равна: {sum}")

sumOddIndex(list)

