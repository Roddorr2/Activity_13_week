# -*- coding: utf-8 -*-
"""MODA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VoC5v0Bts4i6Lf8xZCEW3AOi_oRxH0s3
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, mean, corr
spark = SparkSession.builder.appName('MODA').getOrCreate()

# Cargar el dataset
data = spark.read.csv("Productos.csv", header=True, inferSchema=True, sep=";")

# Identificar la moda del stock de productos registrado, junto con el nombre del producto
stock_mode = data.groupBy("Stock").count().orderBy(col("count").desc()).first()

print(f"Hay {stock_mode[1]} productos con stock más repetidos, con {stock_mode[0]} unidades en stock")