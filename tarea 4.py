import pandas as pd 
import matplotlib.pyplot as plt 

datos = pd.read_csv('titanik.csv')
datos.head()



################################################################### parte 2
media_edad_femenina = datos[datos['gender'] == 'female']['age'].mean()
media_edad_masculina = datos[datos['gender'] == 'male']['age'].mean()
datos.loc[(datos['age'].isnull()) & (datos['gender'] == 'female'), 'age'] = media_edad_femenina
datos.loc[(datos['age'].isnull()) & (datos['gender'] == 'male'), 'age'] = media_edad_masculina

############################################## parte 3 
promedio_edad = datos['age'].mean()
mediana_edad = datos['age'].median()
moda_edad = datos['age'].mode()[0]
rango_edad = datos['age'].max() - datos['age'].min()
varianza_edad = datos['age'].var()
desviacion_edad = datos['age'].std()

print(promedio_edad, mediana_edad, moda_edad, rango_edad, varianza_edad, desviacion_edad)

###################################################### parte 4
tasa_supervivencia_general = datos['survived'].mean()
print(tasa_supervivencia_general)

########################################################parte 5 
tasa_supervivencia_femenina = datos[datos['gender'] == 'female']['survived'].mean()
tasa_supervivencia_masculina = datos[datos['gender'] == 'male']['survived'].mean()
print(tasa_supervivencia_femenina, tasa_supervivencia_masculina)

############################################################## parte 6 
plt.hist(datos[datos['p_class'] == 1]['age'], bins=15, alpha=0.6, label='Primera Clase')
plt.hist(datos[datos['p_class'] == 2]['age'], bins=15, alpha=0.6, label='Segunda Clase')
plt.hist(datos[datos['p_class'] == 3]['age'], bins=15, alpha=0.6, label='Tercera Clase')

plt.legend()
plt.title('Distribución de Edades por Clase')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()

############################################################# parte 7 
datos.boxplot(column='age', by='survived', grid=False)
plt.title('Distribución de Edades por Supervivencia')
plt.suptitle('')
plt.xlabel('Supervivencia (0=No, 1=Sí)')
plt.ylabel('Edad')
plt.show()