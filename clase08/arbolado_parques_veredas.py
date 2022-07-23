import pandas as pd
import os

directorio = '../Data'
archivo1 = 'arbolado-publico-lineal-2017-2018.csv'
archivo2= 'arbolado-en-espacios-verdes.csv'
fname1 = os.path.join(directorio,archivo1)
fname2 = os.path.join(directorio,archivo2)
df_parques= pd.read_csv(fname1)
df_veredas= pd.read_csv(fname2)
cols_sel1= ['altura_arbol', 'diametro_altura_pecho' , 'nombre_cientifico']
cols_sel2= ['altura_tot', 'diametro', 'nombre_cie']
df_tipas_parques  = df_parques[df_parques['nombre_cientifico'] == 'Tipuana tipu'][cols_sel1].copy()
df_tipas_veredas  = df_veredas[df_veredas['nombre_cie'] == 'Tipuana Tipu'][cols_sel2].copy()
df_tipas_veredas.columns=['altura_arbol', 'diametro_altura_pecho', 'nombre_cientifico']
df_tipas_parques=df_tipas_parques.assign(ambiente='parque')
df_tipas_veredas=df_tipas_veredas.assign(ambiente='vereda')
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

df_tipas.boxplot('diametro_altura_pecho',by = 'ambiente')

df_tipas.boxplot('altura_arbol',by = 'ambiente')

def par(n):
    return inpar(n-1)
def inpar(n):
    if n ==0:
        return False
    return par(n-1)

print(inpar(4))
