import pandas as pd

data = pd.read_csv("residuos_original.csv")

# Eliminar duplicados
data = data.drop_duplicates()

# Eliminar pesos negativos
data = data[data["peso"] >= 0]

# Rellenar valores nulos
data["humedad"] = data["humedad"].fillna(data["humedad"].mean())

# Guardar limpio
data.to_csv("residuos_limpios.csv", index=False)
