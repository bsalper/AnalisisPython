import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carga y exploración inicial de los datos:

data_path = "data/tiendita.csv"
data = pd.read_csv(data_path)

print(data.head())
print(data.info())
print(data.describe())

# Conversión de la columna OrderDate a formato de fecha:

data['OrderDate'] = pd.to_datetime(data['OrderDate'])
print(data.info())

# Carga de datos:

# Ventas totales por categoría
sales_by_category = data.groupby("Category")["Price"].sum().sort_values(ascending=False)
print(sales_by_category)
# Ventas totales por cliente
sales_by_customer = data.groupby("CustomerName")["Price"].sum().sort_values(ascending=False)
print(sales_by_customer)
# Ventas a lo largo del tiempo
sales_over_time = data.groupby(data['OrderDate'].dt.to_period("M"))["Price"].sum()
print(sales_over_time)

# Visualización de los datos:

sns.set(style="darkgrid")

# Gráfica de ventas por categoría
plt.figure(figsize=(14, 7))
sns.barplot(x=sales_by_category.index, y=sales_by_category.values, palette="viridis")
plt.title("Ventas Totales por Categoría")
plt.xlabel("Categoría")
plt.ylabel("Ventas Totales")
plt.xticks(rotation=45)
plt.show()
# Gráfica de ventas por cliente
plt.figure(figsize=(14, 7))
sns.barplot(x=sales_by_customer.index, y=sales_by_customer.values, palette="viridis")
plt.title("Ventas Totales por Cliente")
plt.xlabel("Cliente")
plt.ylabel("Ventas Totales")
plt.xticks(rotation=90)
plt.show()
# Gráfica de ventas a lo largo del tiempo
plt.figure(figsize=(14, 7))
sales_over_time.plot()
plt.title("Evolución de las Ventas a lo Largo del Tiempo")
plt.xlabel("Fecha")
plt.ylabel("Ventas Totales")
plt.xticks(rotation=45)
plt.show()


# Interpretación de los datos, ir a archivo "README.md"