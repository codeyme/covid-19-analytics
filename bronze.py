def read_csv_s3(spark):
    hadoop_conf = spark._jsc.hadoopConfiguration()

    hadoop_conf.set("fs.s3a.endpoint", "s3.amazonaws.com")

    nytimes_df = spark.read.csv("s3a://covid-19-analytics-prakriti/bronze/nytimes/us_states.csv", header=True, inferSchema=True)
    nytimes_county_df = spark.read.csv("s3a://covid-19-analytics-prakriti/bronze/nytimes/us_county.csv", header=True,inferSchema=True)
    ctrack_df = spark.read.csv("s3a://covid-19-analytics-prakriti/bronze/covid_tracking/states_daily.csv", header=True, inferSchema=True)
    ctrack_usDaily_df = spark.read.csv("s3a://covid-19-analytics-prakriti/bronze/covid_tracking/us_daily.csv", header=True,inferSchema=True)
    ctrack_us_df = spark.read.csv("s3a://covid-19-analytics-prakriti/bronze/covid_tracking/us.csv",header=True, inferSchema=True)
    static_df = spark.read.csv("s3a://covid-19-analytics-prakriti/bronze/static/states_abv.csv", header=True, inferSchema=True)
    static_qs_df = spark.read.csv("s3a://covid-19-analytics-prakriti/bronze/static/CountryCodeQS.csv", header=True, inferSchema=True)
    static_ppl_df = spark.read.csv("s3a://covid-19-analytics-prakriti/bronze/static/County_Population.csv",header=True, inferSchema=True)
    beds_df = spark.read.json("s3a://covid-19-analytics-prakriti/bronze/hospital_bed/usa-hospital-beds.geojson",header=True, inferSchema=True)