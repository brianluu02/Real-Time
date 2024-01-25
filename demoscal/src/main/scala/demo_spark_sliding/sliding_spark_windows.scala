package demo_spark_sliding

import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.types.{StructField, StructType, TimestampType, StringType}
import org.apache.spark.sql.functions._
import org.apache.spark.sql.streaming._

object sliding_spark_windows extends App {
  val spark = SparkSession.builder().appName(name = "Readfile").master(master = "local[*]").getOrCreate()
//  Đặt cấp độ log của Spark thành "ERROR" để giảm thông tin debug xuất hiện trong quá trình chạy.
  spark.sparkContext.setLogLevel("ERROR")

  val schema = StructType(List(
    StructField("Date", TimestampType, true),
    StructField("Message", StringType, true)
  ))

  val StreamDF = spark.readStream.option("delimiter", "|").schema(schema).csv("D:\\Nam 4\\HK-1\\Real Time\\demoscal\\src\\main")

  StreamDF.createOrReplaceTempView(viewName = "SDF")

  val windowedDF = StreamDF
    .withWatermark("Date", "10 minutes") // Xác định watermark cho cửa sổ thời gian
    .groupBy(window(col("Date"), " 2 minutes", "2 minutes")) // Xác định cửa sổ trượt (5 phút cửa sổ, 1 phút trượt)
    .agg(count("Message").as("MessageCount"))

  val formattedDF = windowedDF.withColumn("window", date_format(col("window.start"), "yyyy-MM-dd HH:mm:ss"))

//  val query = windowedDF.writeStream
  val query = formattedDF.writeStream
    .format("console")
    .outputMode("complete")
    .start()
    .awaitTermination() //để đợi cho đến khi quá trình streaming kết thúc.
}