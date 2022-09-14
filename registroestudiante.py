#REGISTRO ESTUDIANTES

import statistics

#Importación para poder promediar

print('Ingrese alumno y calificaciones para visualizar su condición')

nombre = input('Agregar alumno: ').upper()
materia = input('Ingrese nombre materia: ').capitalize()
notas_practicos = []
notas_parcial = []
promedio_practicos = 0
promedio_parciales = 0

#Bucles para solicitar las 3 calificaciones correspondientes a prácticos y exámenes parciales

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

print(f'las calificaciones en trabajos prácticos de {nombre} en {materia} fueron {notas_practicos}')
print(f'las calificaciones en exámenes parciales de {nombre} en {materia} fueron {notas_parcial}')

#Para ver todas las calificaciones
notas_totales = notas_practicos + notas_parcial

#Para promediar
promedio_practicos = int(statistics.mean(notas_practicos))
promedio_parciales = int(statistics.mean(notas_parcial))

#Para obtener la condición final
def condicion_final():
  for num in notas_totales:
      if num < 4:
        return print(f'{nombre} desaprobó {materia}')
  if promedio_practicos >= 4 and promedio_practicos <= 6 and promedio_parciales >= 4:
    return print(f'{nombre} aprobó {materia}')
  elif promedio_practicos >= 7 and promedio_parciales >= 7:
    return print(f'{nombre} promocionó {materia}')

print(f'Promedio parciales: {promedio_parciales} Promedio practicos: {promedio_practicos}')
condicion_final()



