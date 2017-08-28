# Purpose
To learn how to use psycopg2 to query a mock PostgreSQL database for a fictional news website.  

# How to run
## Download database file and unzip
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

## Load the database from file
```
psql -d news -f newsdata.sql
```

## Connect
```
psql -d news
```

## Create Views
```
psql -d news -f create_views.sql
```

## Run
```
python log.py
```
