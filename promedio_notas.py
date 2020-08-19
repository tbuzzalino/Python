# Promedio notas 

""" Tomas las notas de los alumnos y genera un promedio"""

total = 0 # total de las notas

contador_notas = 0

notas = [98,76,71,87,83,90,57,79,82,94] # lista con 10 notas

for n in notas:
    total += n # suma las notas
    contador_notas += 1 # agrega una nota por iteracion

promedio_notas = total / contador_notas

print(f'El promedio de la clase es de {promedio_notas}.')
