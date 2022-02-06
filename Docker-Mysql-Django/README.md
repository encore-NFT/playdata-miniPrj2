# Docker-Compose-Django

### docker 서버 실행  🚀

```bash
docker-compose up -d db
docker-compose up web
```

`http://localhost:8000/home/`으로 접속

### mysql 서버 접속

```
docker exec -it -e LC_ALL=C.UTF-8 mysqlD bash
```

```
$ mysql -u root -p

>SHOW VARIABLES LIKE "secure_file_priv";
/var/lib/mysql-files/

>CREATE DATABASE newsDB;

>USE newsDB;

>CREATE TABLE news_title (
    news_title VARCHAR(300) NOT NULL,
    news_date VARCHAR(20) NOT NULL
  );
  
>LOAD DATA INFILE '/var/lib/mysql-files/result02.csv'
INTO TABLE news_title
FIELDS TERMINATED BY '\t'
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

```