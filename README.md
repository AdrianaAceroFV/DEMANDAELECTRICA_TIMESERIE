# Series Temporales

## Descripción
Trabajo sobre Series Temporales (modelos de suavizado y modelos ARIMA) realizado para el Máster de Big Data, Data Science e Inteligencia Artificial de la Universidad Complutense de Madrid.


## Contenidos del Repositorio

Los datos elegidos corresponden a la evolución de la demanda eléctrica en España. Han sido obtenidos de la página oficial de la Red Eléctrica Española (https://www.ree.es). Se ha utilizado la documentación de la API disponible (https://www.ree.es/es/apidatos) para solicitar los datos diarios desde el año 2011 a 2023 (ver código de python en api.py). De esta manera, se ha obtenido un csv por año con los datos diarios de la demanda eléctrica.

Una vez obtenidos los datos diarios, se han llevado a cabo un proceso de limpieza del formato de las fechas (ver código en cleaning.py) y concatenación de los datos en un solo archivo. Luego se han seleccionado los valores máximos de cada mes (ver maximos.ipynb) para adecuarlo a la tarea, ya que se requería un conjunto de datos de unos 150 datos observados.


- [Memoria](Adriana_Acero.pdf): Documento completo de la memoria.
- [Script](main.ipynb): Jupyter Notebook de Python con el análisis y código fuente.
- [Datos](demanda_electrica_maxima_mes_2011_2023.csv): Conjunto de datos analizados.
- [Script auxiliar de llamada a la API](api.py)
- [Script auxiliar de limpieza](cleaning.py): Limpia el formato de fechas y concatena los datos en un solo archivo csv.
- [Script auxiliar de selección de datos](maximos.ipynb): Selecciona el valor máximo de cada mes. Se obtiene el conjunto de datos a analizar finales demanda_electrica_maxima_mes_2011_2023.csv.
