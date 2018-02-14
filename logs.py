#!/usr/bin/python3

# importing database interface library.
import psycopg2
import datetime

database = "news"

def find_most_popular_authors(cursor) :
    """ Returns a list containing most popular authors"""
    sql_query = "SELECT name,count(path) AS views FROM authors,articles, log"\
    +" WHERE path = CONCAT('/article/',slug) AND authors.id = author"\
    +" GROUP BY authors.id ORDER BY views DESC"
    cursor.execute(sql_query)
    return cursor.fetchall()

def find_most_popular_articles(cursor):
    """ Returns a list containing most popular artilces"""
    sql_query = "SELECT title,count(path) AS views FROM articles, log"\
    +" WHERE path = CONCAT('/article/',slug)"\
    +" GROUP BY articles.id ORDER BY views DESC LIMIT 3"
    cursor.execute(sql_query)
    return cursor.fetchall()

def find_error(cursor):
    """ Returns a List containing days with 404 error greater than 1%"""
    view_success = "CREATE OR REPLACE VIEW LOG_SUCCESS AS SELECT DATE(time) "\
    +"AS day, COUNT(*) AS num_total FROM log GROUP BY DATE(time)"
    view_failure = "CREATE OR REPLACE VIEW LOG_FAILED AS SELECT DATE(time) "\
    +"AS day, COUNT(*) AS num_failed FROM log WHERE status = '404 NOT FOUND'"\
    +" GROUP BY DATE(time)"
    sql_query = "SELECT DATE(time) AS day,num_failed::float/num_total * 100 AS"\
    +" failure_percent FROM log,LOG_SUCCESS,LOG_FAILED"\
    +" WHERE DATE(time) = LOG_SUCCESS.day AND DATE(time) = LOG_FAILED.day"\
    +" AND (num_failed::float/num_total * 100) >= 1"\
    +" GROUP BY DATE(time),num_failed,num_total"
    cursor.execute(view_success)
    cursor.execute(view_failure)
    cursor.execute(sql_query)
    return cursor.fetchall()

def main() :
    """Main program which displays output for Log Analysis Project"""
    connection = psycopg2.connect(database=database)
    cursor = connection.cursor()
    most_articles = find_most_popular_articles(cursor)
    # QUESTION:  Solving for question_1
    question_1 = "1. What are the most popular three articles of all time?"
    print(question_1)
    print("")
    print("%-35s %-10s" %("Article Title","Views"))
    print("=================================== =========")
    for article in most_articles:
        print("%-35s %-10d" %(article[0],article[1]))
    print("")
    print("--------------------------------------")
    # QUESTION: Solution for question_2
    most_popular = find_most_popular_authors(cursor)
    question_2 = "2. Who are the most popular article authors of all time?"
    print("")
    print(question_2)
    print("")
    print("%-25s %-10s" %("Author name","Views"))
    print("======================== =========")
    for author in most_popular:
        print("%-25s %-10d" %(author[0],author[1]))
    print(" ")
    print("--------------------------------------")
    # QUESTION: Solution for question_3
    question_3 = "3. On which days did more than 1% of requests lead to errors?"
    print("")
    print(question_3)
    print("")
    errors = find_error(cursor)
    print("%-20s %-10s" %("Date","Error Percent"))
    print("===================  =========")
    for error in errors:
        print("%-20s %-3.1f%%" %(error[0].strftime('%B %-d, %Y'),error[1]))

    connection.close()

if __name__ == "__main__" :
    main()
