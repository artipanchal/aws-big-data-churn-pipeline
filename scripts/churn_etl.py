from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("Telco-Churn-Automation").getOrCreate()

RAW_PATH = "s3a://bigdata-arti-churn/processed/telco_churn.csv"
OUT_PATH = "s3a://bigdata-arti-churn/processed/clean_parquet/"

df = spark.read.option("header", True).option("inferSchema", True).csv(RAW_PATH)
def norm(c):
    return c.strip().lower().replace(" ", "_")

df = df.toDF(*[norm(c) for c in df.columns])

df = df.withColumn("total_charges", F.col("total_charges").cast("string"))
df = df.withColumn(
    "total_charges",
    F.when(F.col("total_charges") == "", None)
     .otherwise(F.col("total_charges"))
     .cast("double")
).fillna({"total_charges": 0.0})

df = df.withColumn("monthly_charges", F.col("monthly_charges").cast("double")) \
       .withColumn("tenure_months", F.col("tenure_months").cast("int")) \
       .withColumn("churn_value", F.col("churn_value").cast("int"))

df = df.dropDuplicates(["customerid"])

df = df.withColumn(
    "tenure_group",
    F.when(F.col("tenure_months") < 12, "0-11")
     .when(F.col("tenure_months") < 24, "12-23")
     .when(F.col("tenure_months") < 48, "24-47")
     .otherwise("48+")
)

df = df.withColumn(
    "monthly_charge_level",
    F.when(F.col("monthly_charges") < 35, "Low")
     .when(F.col("monthly_charges") < 70, "Medium")
     .otherwise("High")
)

df.write.mode("overwrite").parquet(OUT_PATH)

spark.stop()
