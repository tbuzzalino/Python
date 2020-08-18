# comparando_numeros.py

""" Con este script lo que vamos a hacer es comparar 2 numeros y ver si tienen cosas en comun"""

print('Ingresa dos numeros enteros y vamos a compararlos.')

num1 = int(input('Ingresa el primer numero: '))

num2 = int(input('Ingresa el segundo numero: '))

if num1 == num2:
    print(num1 , 'es igual a', num2)
    
if num1 != num2:
    print('Los numeros que ingresaste son distintos.') 
    
if num1 < num2:
    print('El numero que ingresaste primero es mas chico que el segundo numero.')

if num1 > num2:
    print('El primer numero es mayor al segundo numero.')    
    
if num1 >= num2:
    print('El primer numero que ingresaste es igual o mayor que el segundo numero.')
    
if num1 <= num2:
    print('El segundo numero que ingresaste es igual o mayor que el primer numero.')
    
    