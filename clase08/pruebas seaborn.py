import pandas as pd
import os
import seaborn as sns

directorio = '../Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio,archivo)
df_lineal= pd.read_csv(fname)
cols_sel= ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
lista=df_lineal[cols_sel]
print(lista)
cant_ejemplares = df_lineal['nombre_cientifico'].value_counts()
print(cant_ejemplares.head(10))
especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]
print(df_lineal_seleccion)
df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')
sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')