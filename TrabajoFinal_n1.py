#Trabajo final Datux Python - Ejercicio 1_DataFrames y Series

#Importar pandas

import os
import pandas as pd

#Crear una serie

#Serie de los números 10, 20, 10

numeros={'1°': 10, '2°': 20, '3°': 10}
serie1=pd.Series(data=numeros, index=['1°', '2°', '3°'])
serie1

#Serie con tres objetos "rojo", "verde", "azul"

colores={'color 1': "rojo", 'color 2': "verde", 'color 3': "azul"}
serie2=pd.Series(data=colores, index=['color 1', 'color 2', 'color 3'])
serie2

#Crear un dataframe

#Dataframe vacío llamado 'df'

import pandas as pd
df=pd.DataFrame()


# Creación de una nueva columna en el dataframe, y asignale la primera serie que se ha creado

import os
import pandas as pd
numeros={'1°': 10, '2°': 20, '3°': 10}
serie1=pd.Series(data=numeros, index=['1°', '2°', '3°'])

df=pd.DataFrame({'Columna 1': serie1})
print(df)

# Creación de otra columna en el dataframe, y asignar la segunda serie que se ha creado

import os
import pandas as pd

numeros={'1°': 10, '2°': 20, '3°': 10}
serie1=pd.Series(data=numeros, index=['1°', '2°', '3°'])

colores={'color 1': "rojo", 'color 2': "verde", 'color 3': "azul"}
serie2=pd.Series(data=colores, index=['color 1', 'color 2', 'color 3'])

df=pd.DataFrame({'Columna 1': serie1, 'Columna 2': serie2})
print(df)

#Leer un DataFrame

# Leer el archivo llamado 'avengers.csv" localizado en la carpeta "data"
# y crea un DataFrame, llamado 'avengers'. 
# El archivo está localizado en "data/avengers.csv".

import pandas as pd

df=pd.read_csv('C:/Users/moseb/Documents/Datux/Python/TrabajoFinal_Datux_Python/FinalPython/src/pandas/avengers.csv', sep=',')
print(df)

#Inspeccionar un DataFrame

# Muestra las primeras 5 filas del DataFrame.
 
import pandas as pd

df=pd.read_csv('C:/Users/moseb/Documents/Datux/Python/TrabajoFinal_Datux_Python/FinalPython/src/pandas/avengers.csv', sep=',')
df.head()

# Muestra las primeras 10 filas del DataFrame

import pandas as pd
df=pd.read_csv('C:/Users/moseb/Documents/Datux/Python/TrabajoFinal_Datux_Python/FinalPython/src/pandas/avengers.csv', sep=',')
df.head(10)

# Muestra las últimas 5 filas del DataFrame

import pandas as pd
df=pd.read_csv('C:/Users/moseb/Documents/Datux/Python/TrabajoFinal_Datux_Python/FinalPython/src/pandas/avengers.csv', sep=',')
df.tail()

#Tamaño del DataFrame

# Muestra el tamaño del DataFrame

import pandas as pd
df=pd.read_csv('C:/Users/moseb/Documents/Datux/Python/TrabajoFinal_Datux_Python/FinalPython/src/pandas/avengers.csv', sep=',')
df.shape


#Data types en un DataFrame

# Muestra los data types del dataframe

import pandas as pd
df=pd.read_csv('C:/Users/moseb/Documents/Datux/Python/TrabajoFinal_Datux_Python/FinalPython/src/pandas/avengers.csv', sep=',')
df.dtypes


#Editar el indice (index)

# Cambia el indice a la columna "fecha_inicio".

import pandas as pd
df=pd.read_csv('C:/Users/moseb/Documents/Datux/Python/TrabajoFinal_Datux_Python/FinalPython/src/pandas/avengers.csv', sep=',')
df.set_index('fecha_inicio')


#Ordenar el indice

# Ordena el índice de forma descendente

import pandas as pd
import numpy as np

df=pd.read_csv('C:/Users/moseb/Documents/Datux/Python/TrabajoFinal_Datux_Python/FinalPython/src/pandas/avengers.csv', sep=',')
df.sort_values(by=['fecha_inicio'], ascending=[False])


#Resetear el indice

# Resetea el indice

import pandas as pd
import numpy as np

df=pd.read_csv('C:/Users/moseb/Documents/Datux/Python/TrabajoFinal_Datux_Python/FinalPython/src/pandas/avengers.csv', sep=',')
df.sort_values(by=['fecha_inicio'], ascending=[False])
df.reset_index()



