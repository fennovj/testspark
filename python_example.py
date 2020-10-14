# Note: See installing.md to see how to get this code working
from pyspark.sql import SparkSession
import logging

# Default spark session. Master is configured in the spark-submit command line (see installing.md)
# But can also be configured as `SparkSession.builder.master('spark://xxx:7077').getOrCreate()`
spark = SparkSession.builder.getOrCreate()

data_url = 'https://raw.githubusercontent.com/databricks/Spark-The-Definitive-Guide/master/data/flight-data/csv/2015-summary.csv'

flightData2015 = spark \
    .read \
    .option("inferSchema","true") \
    .option("header","true") \
    .csv("data/2015-summary.csv")

flightData2015.take(3)