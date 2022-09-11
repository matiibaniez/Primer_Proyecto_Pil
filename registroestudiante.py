#REGISTRO ESTUDIANTES

import statistics

print('Ingrese alumnos, si no desea agregar mas, escriba "salir"')

nombre = input('Agregar alumno: ').upper()
materia = input('Ingrese nombre materia: ').capitalize()
notas_practicos = []
notas_parcial = []
promedio_practicos = 0
promedio_parciales = 0



for i in range(3):
  try:
    notas = int(input(f'Ingresar nota practico {i+1}: '))
    if notas > 10:
      notas = (int(input(f'Ingresar nota practico valida {i+1}: ')))
      notas_practicos.append(notas)
    else:
      notas_practicos.append(notas)
  except:
    print('Ingrese una nota valida (0 - 10)')
  

for i in range(3):
  try:
    notas = int(input(f'Ingresar nota parcial {i+1}: '))
    if notas > 10:
      notas = (int(input(f'Ingresar nota parcial valida {i+1}: ')))
      notas_parcial.append(notas)
    else:
      notas_parcial.append(notas)
  except:
    print('Ingrese una nota valida (0 - 10)')

print(notas_practicos)
print(notas_parcial)

notas_totales = notas_practicos + notas_parcial

promedio_practicos = statistics.mean(notas_practicos)
promedio_parciales = statistics.mean(notas_parcial)


def condicion_final():
  for num in notas_totales:
      if num < 4:
        return print(f'{nombre} desaprobo {materia}')
  if promedio_practicos >= 4 and promedio_practicos <= 6 and promedio_parciales >= 4:
    return print(f'{nombre} aprobo {materia}')
  elif promedio_practicos >= 7 and promedio_parciales >= 7:
    return print(f'{nombre} promociono {materia}')

print(f'Promedio parciales: {promedio_parciales} Promedio practicos: {promedio_practicos}')
condicion_final()



