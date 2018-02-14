# Udacity Logs
Third project for Udacity Fullstack Nanodegree.

Requirements
1. Python.
1. [PostgreSQL](https://www.postgresql.org/) should be installed.
1. [Psycopg2](http://initd.org/psycopg/) should be installed.
1. Create Database named **news** using
  ``` createdb news``` command.
1. Clone the repo using git clone or Download the zip and extact.
1. ```cd``` to the repo.
1. Now import the data to the database using ```
psql -d news -f newsdata.sql``` command. (Note newsdata.sql can be found in this repo.)

Run the script using ``` python3 logs.py ```.

Note for the 3rd problem some SQL views are created
They are.
1. ``` CREATE VIEW LOG_SUCCESS AS SELECT DATE(time) AS day, COUNT(*) AS num_total FROM log GROUP BY DATE(time);```
1. ``` CREATE VIEW LOG_FAILED AS SELECT DATE(time) AS day, COUNT(*) AS num_failed FROM log WHERE status = '404 NOT FOUND' GROUP BY DATE(time);```


* **LOG_SUCCESS** contains total requests for each day.
* **LOG_FAILED** contains all requests failed for each day.

### Output

```
1. What are the most popular three articles of all time?

Article Title                       Views     
=================================== =========
Candidate is jerk, alleges rival    338647    
Bears love berries, alleges bear    253801    
Bad things gone, say good people    170098    

--------------------------------------

2. Who are the most popular article authors of all time?

Author name               Views     
======================== =========
Ursula La Multa           507594    
Rudolf von Treppenwitz    423457    
Anonymous Contributor     170098    
Markoff Chaney            84557     

--------------------------------------

3. On which days did more than 1% of requests lead to errors?

Date                 Error Percent
===================  =========
July 17, 2016        2.3%

```
