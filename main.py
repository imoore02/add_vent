"""
Phase 1: Implement a NLP AI to scan text and produce structured output about the dates present.

"""
# import package Spark NLP for extraction of dates. Find documentation here: https://www.johnsnowlabs.com/extracting-exact-dates-from-natural-language-text/
import sparknlp

from sparknlp.annotator import DocumentAssembler, DateMatcher, MultiDateMatcher
from pyspark.sql.types import StringType
from pyspark.ml import Pipeline

spark = sparknlp.start(apple_silicon=True)
spark
documentAssembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

date = DateMatcher() \
    .setInputCols("document") \
    .setOutputCol("date") \
    .setOutputFormat("yyyy/MM/dd")

multiDate = MultiDateMatcher() \
    .setInputCols("document") \
    .setOutputCol("multi_date") \
    .setOutputFormat("MM/dd/yy")


pipeline = Pipeline().setStages([
    documentAssembler,
    date,
    multiDate
    ])

text_list = ["See you on next monday.",  
             "She was born on 02/03/1966.", 
             "The project started yesterday and will finish next year.", 
             "She will graduate by July 2023.", 
             "She will visit doctor tomorrow and next month again."]

spark_df = spark.createDataFrame(text_list, StringType()).toDF("text")

result = pipeline.fit(spark_df).transform(spark_df)
result.selectExpr("text","date.result as date", "multi_date.result as multi_date").show(truncate=False)