import numpy as np

# Datos para la Línea 1 y Línea 2
probabilidades = [0.05, 0.15, 0.60, 0.15, 0.05]
rendimientos_linea1 = [0.01, 0.01, 0.09, 0.15, 0.16]
rendimientos_linea2 = [0.01, 0.25, 0.80, 0.14, 0.15]

# Calculo del valor esperado de rendimiento para cada línea
valor_esperado_linea1 = sum([p * r for p, r in zip(probabilidades, rendimientos_linea1)])
valor_esperado_linea2 = sum([p * r for p, r in zip(probabilidades, rendimientos_linea2)])

print(f'Valor esperado linea 1: {valor_esperado_linea1}')
print(f'Valor esperado linea 2: {valor_esperado_linea2}\n') 

# Calculamos la desviación estándar para cada línea utilizando las probabilidades y los rendimientos
# Primero, para la Línea 1
desviaciones_linea1 = [(r - valor_esperado_linea1) ** 2 for r in rendimientos_linea1]
varianza_linea1 = sum([p * d for p, d in zip(probabilidades, desviaciones_linea1)])
desviacion_estandar_linea1 = np.sqrt(varianza_linea1)

# Ahora, para la Línea 2
desviaciones_linea2 = [(r - valor_esperado_linea2) ** 2 for r in rendimientos_linea2]
varianza_linea2 = sum([p * d for p, d in zip(probabilidades, desviaciones_linea2)])
desviacion_estandar_linea2 = np.sqrt(varianza_linea2)

print(f'Desviacion estandar linea 1: {desviacion_estandar_linea1}')
print(f'Desviacion estandar linea 2: {desviacion_estandar_linea2}\n')

#Calculamos el coeficiente de variabilidad para cada linea:
CV1=(desviacion_estandar_linea1/valor_esperado_linea1)*100
CV2=(desviacion_estandar_linea2/valor_esperado_linea2)*100

print(f'Coeficiente de variabilidad linea 1={CV1}')
print(f'Coeficiente de variabilidad linea 2={CV2}')