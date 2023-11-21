## ST0263 Temas especiales en telemática

#

## Sara María Castrillón Ríos - smcastril1@eafit.edu.co

#

## Edwin Nelson Montoya Múnera - emontoya@eafit.edu.co

#

## Laboratorio2 - Spark:

#

1. Via pyspark en el nodo master:
   ![Alt text](1.png)

2. Correrlo como un archivo python:

```
spark-submit --master yarn --deploy-mode cluster wc-pyspark.py
```

![Alt text](2.png)
![Alt text](6.png)

3. Correrlo desde un Zeppelin notebook:

3.1 Cree un notebook:
![Alt text](4.png)

3.2 Wordcount en python:

![Alt text](5.png)

```
%spark.pyspark
# WORDCOUNT COMPACTO
#files_rdd = sc.textFile("s3://st0263datasets/gutenberg-small/*.txt")
files_rdd = sc.textFile("hdfs:///datasets/gutenberg-small/*.txt")
wc_unsort = files_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
wc = wc_unsort.sortBy(lambda a: -a[1])
for tupla in wc.take(10):
    print(tupla)
    wc.coalesce(1).saveAsTextFile("hdfs:///tmp/wcout1")
```

![Alt text](6.png)

4. Jupyter Notebooks en EMR:
   ![Alt text](7.png)
   ![Alt text](8.png)
   ![Alt text](9.png)
   ![Alt text](11.png)
   ![Alt text](12.png)
   ![Alt text](13.png)
