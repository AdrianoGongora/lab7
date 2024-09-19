import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

file_path = "./BI_Alumnos07-1.xlsx"
df = pd.read_excel(file_path)

print(df.head())  # Verifica que los datos se han cargado correctamente

# Verifica si hay valores faltantes
print(df.isnull().sum())

X = df[['Altura']]  # Variable independiente
y = df['Peso']     # Variable dependiente

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

# Ajustar el modelo
model.fit(X_train, y_train)

# Imprimir el coeficiente y la intersección
print(f"Coeficiente (pendiente): {model.coef_[0]}")
print(f"Intersección: {model.intercept_}")

# Hacer predicciones
y_pred = model.predict(X_test)

# Mostrar resultados
result_df = pd.DataFrame({'Valor Real': y_test, 'Predicción': y_pred})
print(result_df)

# Visualizar los resultados
plt.scatter(X_test, y_test, color='blue', label='Valores Reales')
plt.plot(np.sort(X_test.values.ravel()), model.predict(np.sort(X_test.values.ravel()).reshape(-1, 1)), color='red', label='Predicción')
plt.xlabel('Altura')
plt.ylabel('Peso')
plt.legend()
plt.show()

# Evaluar el modelo
r2 = r2_score(y_test, y_pred)
print(f"R^2 score: {r2}")
