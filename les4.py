# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = int(input("Введите десятичное число:\n"))
binary = ""

while number != 0:
    binary = str(number%2) + binary
    number //=2

print(binary)