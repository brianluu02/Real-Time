package BT_Tuan4

import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions.{explode, split}

object Demo_Netcat {
  def main(args: Array[String]): Unit = {

    // Khởi tạo SparkSession
    val spark: SparkSession = SparkSession.builder()
      .master("local[5]")
      .appName("Demo_Spark + Netcat")
      .getOrCreate()
    //hiển thị log cấp độ lỗi để giảm sự nhiễu loạn
    spark.sparkContext.setLogLevel("ERROR")
    // Đọc dữ liệu từ socket cổng 9999
    val df = spark.readStream
      .format("socket")
      .option("host", "localhost")
      .option("port", "9999")
      .load()

    // Tách cột value thành các từ
    val wordsDF = df.select(explode(split(df("value"), " ")).alias("word"))
    // Nhóm các từ và đếm
    val count = wordsDF.groupBy("word").count()
    // Ghi kết quả ra console
    val query = count.writeStream
      .format("console")
      .outputMode("complete")
      .start()
      .awaitTermination()
  }
}
