import math
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

datos = pd.read_csv('titanik.csv')
datos.head()


# parte 2
media_edad_femenina = datos[datos['gender'] == 'female']['age'].mean()
media_edad_masculina = datos[datos['gender'] == 'male']['age'].mean()
datos.loc[(datos['age'].isnull()) & (datos['gender']
                                     == 'female'), 'age'] = media_edad_femenina
datos.loc[(datos['age'].isnull()) & (datos['gender']
                                     == 'male'), 'age'] = media_edad_masculina

# parte 3
promedio_edad = datos['age'].mean()
cantidad_personas = datos['age'].count()
cantidad_mujeres = (datos['gender'] == 'female').sum()
cantidad_hombres = (datos['gender'] == 'male').sum()
mediana_edad = datos['age'].median()
moda_edad = datos['age'].mode()[0]
rango_edad = datos['age'].max() - datos['age'].min()
varianza_edad = datos['age'].var()
desviacion_edad = datos['age'].std()

print("Promedio de edad:", promedio_edad)
print("Mediana de edad:", mediana_edad)
print("Moda de edad:", moda_edad)
print("Rango de edad:", rango_edad)
print("Varianza de edad:", varianza_edad)
print("Desviacion estandar de edad:", desviacion_edad)

# parte 4
tasa_supervivencia_general = datos['survived'].mean()
print("Tasa supervivencia general:", tasa_supervivencia_general)

# parte 5
tasa_supervivencia_femenina = datos[datos['gender']
                                    == 'female']['survived'].mean()
tasa_supervivencia_masculina = datos[datos['gender']
                                     == 'male']['survived'].mean()
print("Tasa supervivencia femenina:", tasa_supervivencia_femenina)
print("Tasa supervivencia masculina:", tasa_supervivencia_masculina)

# parte 6
plt.hist(datos[datos['p_class'] == 1]['age'],
         bins=15, alpha=0.6, label='Primera Clase')
plt.hist(datos[datos['p_class'] == 2]['age'],
         bins=15, alpha=0.6, label='Segunda Clase')
plt.hist(datos[datos['p_class'] == 3]['age'],
         bins=15, alpha=0.6, label='Tercera Clase')

plt.legend()
plt.title('Distribución de Edades por Clase')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()

# parte 7
datos.boxplot(column='age', by='survived', grid=False)
plt.title('Distribución de Edades por Supervivencia')
plt.suptitle('')
plt.xlabel('Supervivencia (0=No, 1=Sí)')
plt.ylabel('Edad')
plt.show()

# parte 1 Ej2
raiz_cantidad_personas = math.sqrt(cantidad_personas)
intervalo_confianza_mayor = (
    promedio_edad + (1.96 * (desviacion_edad / raiz_cantidad_personas)))
intervalo_confianza_menor = (
    promedio_edad - (1.96 * (desviacion_edad / raiz_cantidad_personas)))
print("intervalo: ", intervalo_confianza_menor, intervalo_confianza_mayor)

# parte 2 Ej2

mujeres_interesadas = datos[(datos['gender'] == 'female') & (datos['age'].notnull())]
promedio_edad_mujeres = mujeres_interesadas['age'].mean()
desviacion_mujeres = mujeres_interesadas['age'].std()
cantidad_mujeres = len(mujeres_interesadas)

raiz_cantidad_mujeres = math.sqrt(cantidad_mujeres)
error_estandar_mujeres = desviacion_mujeres / raiz_cantidad_mujeres
print(error_estandar_mujeres, promedio_edad_mujeres)
intervalo_confianza_mayor_mujer = promedio_edad_mujeres + (1.96 * error_estandar_mujeres)
intervalo_confianza_menor_mujer = promedio_edad_mujeres - (1.96 * error_estandar_mujeres)

hombres_interesadas = datos[(datos['gender'] == 'male') & (datos['age'].notnull())]
promedio_edad_hombres = hombres_interesadas['age'].mean()
desviacion_hombres = hombres_interesadas['age'].std()
cantidad_hombres = len(hombres_interesadas)

raiz_cantidad_hombres = math.sqrt(cantidad_hombres)
error_estandar_hombres = desviacion_hombres / raiz_cantidad_hombres
print(error_estandar_hombres, promedio_edad_hombres)
intervalo_confianza_mayor_hombre = promedio_edad_hombres + (1.96 * error_estandar_hombres)
intervalo_confianza_menor_hombre = promedio_edad_hombres - (1.96 * error_estandar_hombres)

resultado_ttest_edad_genero = stats.ttest_ind(datos[datos['gender'] == 'female']['age'], datos[datos['gender'] == 'male']['age'])
p_valor = resultado_ttest_edad_genero.pvalue
print(f"Valor p obtenido: {p_valor}")
