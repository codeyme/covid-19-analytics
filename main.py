from pyspark.sql import SparkSession
from bronze import *
# pyspark --packages org.apache.hadoop: hadoop-aws:3.3.4

if __name__ == '__main__':
    spark:SparkSession = SparkSession.builder.master('local[1]').appName('covid-minimal').enableHiveSupport().getOrCreate()


