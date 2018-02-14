#!/usr/bin/python3

# importing database interface library.
import psycopg2

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

def main() :
    connection = psycopg2.connect(database=database)
    cursor = connection.cursor()
    most_articles = find_most_popular_articles(cursor)
    question_1 = "1. What are the most popular three articles of all time?"
    print(question_1)
    print("")
    print("%-35s %-10s" %("Article Title","Views"))
    print("=================================== =========")
    for article in most_articles:
        print("%-35s %-10d" %(article[0],article[1]))
    print("")
    print("--------------------------------------")
    most_popular = find_most_popular_authors(cursor)
    question_2 = "2. Who are the most popular article authors of all time?"
    print("")
    print(question_2)
    print("")
    print("%-25s %-10s" %("Author name","Views"))
    print("======================== =========")
    for author in most_popular:
        print("%-25s %-10d" %(author[0],author[1]))
    connection.close()

if __name__ == "__main__" :
    main()
