from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

#Variables
kafka_topic = 'mocked_data'


#Methods
def init_spark():
    print("Creating session wich name is EDEM_APP")  
    spark = SparkSession.builder.appName("EDEM_APP").getOrCreate()
    return spark

def main():
    spark=init_spark()

    # Pull data from Kafka topic
    

    df = spark.readStream.format("kafka")\
                     .option("kafka.bootstrap.servers", "kafka0:29092")\
                     .option("subscribe", kafka_topic)\
                     .option("startingOffsets", "earliest")\
                     .load()
    df = df.selectExpr("CAST(value AS STRING)")
    
    schema = StructType([ \
        StructField("name",StringType()), \
        StructField("age",StringType()), \
        StructField("city",StringType()) ])

    df_1 = df.select(from_json("value", schema).alias("schema_data"))

    df_2 = df_1.select("schema_data.*")

    print("printing Schema of Ejemplo")
    df_2.printSchema()

    # Almacena la salida de uno o más tópicos en Kafka
    query = df_2.writeStream.outputMode("append").format("memory").queryName("testk2s").option("partition.assignment.strategy", "range").start()

    query.awaitTermination(30)

    query.stop()

    query.status

    # Query data
    test_result=spark.sql("select * from testk2s")
    test_result.show(5)

    spark.sql("select count(*) from testk2s").show()
    test_result_small = spark.sql("select * from testk2s limit 5")
    test_result_small.show()

    df_2.printSchema()
    
    
 
if __name__ == '__main__':
  main()

