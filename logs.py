#!/usr/bin/env python2

import psycopg2

question_1 = """
select title, count(*) as views from articles inner join
log on log.path = concat('/article/', articles.slug)
where log.status like '%200%'
group by log.path, articles.title order by views desc limit 3;
"""

question_2 = """
select authors.name, count(*) as views from articles inner join
authors on  authors.id = articles.author inner join
log on log.path = concat('/article/', articles.slug) where
log.status like '%200%' group by authors.name order by views desc;
"""

question_3 = """
select *
from error
where error.percentage > 1
order by error.percentage desc;
"""


def query(thing):
    try:
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
        c.execute(thing)
        data = c.fetchall()
        db.close()
        return data
     except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def question1():
    """Prints top three most popular articles"""
    print "1. What are the most popular three articles of all time?"
    q1 = query(question_1)
    for title, views in q1:
        print('\"{}\" - {} views'.format(title, views))
    print("\n")


def question2():
    """Prints most popular article authors"""
    print "2. Who are the most popular article authors of all time?"
    q2 = query(question_2)
    for title, views in q2:
        print('\"{}\" - {} views'.format(title, views))
    print("\n")


def question3():
    """Prints when error was more than 1%"""
    print "3. On which days did more than 1% of requests lead to errors?"
    q3 = query(question_3)
    for i in range(0, len(q3)):
        print str(q3[i][0]) + " - " + str(round(q3[i][1], 2)) + "% errors"
    print("\n")


if __name__ == '__main__':
    question1()
    question2()
    question3()
