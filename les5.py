# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

k = int(input("Введите число: "))

def fibo(k):
    if k >= 0:
       idx = range(k + 1)
       x = [0,1]
       for n in idx[2:]:
           x.append(x[n-1] + x[n-2]) 
       return x[k]
    else:
       k =- (k - 1)
       idx = range(k + 1)
       x = [1, 0]
       for n in idx[2:]:
           x.append(x[n - 2] - x[n - 1]) 
       x.reverse()
    return x[0]

for i in range(-k, k+1):
   print(fibo(i))



 

