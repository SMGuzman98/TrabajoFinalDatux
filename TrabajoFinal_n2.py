#Trabajo final Datux Python - Filtrado de DataFrames y Series

#Ejercicio - Búsqueda de alojamiento en Airbnb

import pandas as pd
df_airbnb=pd.read_csv('C:/Users/moseb/Documents/Datux/Python/TrabajoFinal_Datux_Python/FinalPython/src/pandas/airbnb.csv', sep=',')
df_airbnb.head()

df_airbnb.dtypes


#Caso 1

condicion1=(df_airbnb.room_type=="Private room") & (df_airbnb.reviews>10) & (df_airbnb.overall_satisfaction>4)
df_airbnb[condicion1]

df_sorted=df_airbnb[condicion1].sort_values(by=["overall_satisfaction", "reviews"], ascending=[False, False])
df_sorted.head(3)


#Caso 2

condicion2=(df_airbnb.room_id==97503) | (df_airbnb.room_id==90387)
df_airbnb[condicion2]
df_airbnb[condicion2].to_excel('C:/Users/moseb/Documents/Datux/Python/TrabajoFinal_Datux_Python/FinalPython/src/pandas/roberto.xlsx',
sheet_name='data', encoding='utf-8', index=False)


#Caso 3

#Se divide los 50 euros entre 3 para hallar el precio que gastaría Diana en una noche de alojamiento

condicion3=(df_airbnb.room_type=="Shared room") & (df_airbnb.price<=16.67)
df_airbnb[condicion3]

df_sorted=df_airbnb[condicion3].sort_values(by=["price", "overall_satisfaction"], ascending=[True, False])
df_sorted.head(10)



#Usando MatPlot

#Caso 1

import pandas as pd
import matplotlib.pyplot as plt

df_airbnb=pd.read_csv('C:/Users/moseb/Documents/Datux/Python/TrabajoFinal_Datux_Python/FinalPython/src/pandas/airbnb.csv', sep=',')
tipo_cuarto=df_airbnb[['room_type']]
gr=tipo_cuarto.value_counts().plot.pie()




