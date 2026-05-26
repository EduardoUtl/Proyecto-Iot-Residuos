import pandas as pd
import matplotlib.pyplot as plt

# Cargar dataset limpio
data = pd.read_csv("residuos_limpios.csv")

# Mostrar primeras filas
print("Primeros registros:")
print(data.head())

# Contar residuos por categoría
conteo = data["clasificacion"].value_counts()

print("\nCantidad de residuos por categoría:")
print(conteo)

# Promedio de humedad
promedio_humedad = data["humedad"].mean()

print("\nPromedio de humedad:")
print(round(promedio_humedad, 2))

# Promedio de peso
promedio_peso = data["peso"].mean()

print("\nPromedio de peso:")
print(round(promedio_peso, 2))

# Cantidad de metales detectados
metales = data["metal"].sum()

print("\nCantidad de residuos metálicos:")
print(metales)

# Crear gráfica
conteo.plot(kind="bar")

plt.title("Clasificación de residuos")
plt.xlabel("Categoría")
plt.ylabel("Cantidad")

plt.show()
