
from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns

# Se importan los datos de las 150 flores Iris (3 especies)
iris_dataset = load_iris()  

# creamos un dataframe de los datos de flores
# etiquetamos las columnas usando las cadenas de iris_dataset.feature_names
iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)

# Le agrego al dataframe 'iris_dataframe' la columna/atributo 'target' 
# que indica la especie de cada flor con valores 0= setosa,1= versicolor 
# y 2= virginica
iris_dataframe['target'] = iris_dataset['target']

# y hacemos una matriz de gráficos de dispersión usando Pandas, asignando colores según la especie con el comando c = iris_dataset['target']
pd.plotting.scatter_matrix(iris_dataframe, c = iris_dataset['target'], figsize = (15, 15), marker = 'o', hist_kwds = {'bins': 20}, s = 60, alpha = 0.8)


# Seteo hue sobre las especies de iris (atributo/columna 'target') para poder identificarlas con
# distintos colores usando Seaborn
sns.pairplot(data = iris_dataframe, hue = 'target')


# Los graficos sin identificar las especies serían
# pd.plotting.scatter_matrix(iris_dataframe, figsize = (15, 15), marker = 'o', hist_kwds = {'bins': 20}, s = 60, alpha = 0.8)
# sns.pairplot(data = iris_dataframe)