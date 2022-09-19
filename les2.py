# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list = list(map(int, input("Введите числа через пробел:\n").split()))

def product_list(list):
    l = len(list)//2 + 1 if len(list) % 2 != 0 else len(list)//2
    new_list = [list[i]*list[len(list)-i-1] for i in range(l)]
    print("Произведения пар чисел: ")
    print(new_list)

product_list(list)