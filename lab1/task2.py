
import math

x=float(input("Введите значение переменной x: "))
y=float(input("Введите значение переменной y: "))
z=float(input("Введите значение переменной z: "))

a = ((x**3/2)**0.5) - math.sin(y)
b = math.exp(2/3)-math.cos(y)+z+math.log(y)


print(f"Получено значение функции a={a}")

