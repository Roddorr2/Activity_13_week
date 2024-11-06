# -*- coding: utf-8 -*-
"""MEDIANA.ipynb

Se busca hallar el número total de filas para así calcular con precisión la mediana del stock de productos

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FCyhGey-7Z2cljHoc7Aab106Z-7kgXmw
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, mean, corr
spark = SparkSession.builder.appName('MEDIANA').getOrCreate()

data = spark.read.csv('Productos.csv', inferSchema=True, header=True, sep=";")

# Conteo de filas
rows = data.count()

stock_median = data.approxQuantile("Stock", [0.5], 0.0)

data.show()
print(f"Hay {rows} filas, del cual el valor de la mediana del stock es {stock_median}")
