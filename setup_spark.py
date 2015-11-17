# Spark setup script for notebook with Spark Standalone running locally
from pyspark import SparkConf, SparkContext
conf = SparkConf()
conf.setMaster('local')
conf.set('spark.cores.max', '1')
#conf.set('spark.executor.memory', '5g')
conf.set('spark.driver.memory', '128m')
sc = SparkContext(conf=conf)

from pyspark.sql import SQLContext
import pyspark.sql.functions as F
