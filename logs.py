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
    except:
        print ("There was an error")


def question1():
    #Answer to question 1
    print "1. What are the most popular three articles of all time?"
    q1 = query(question_1)
    for i in range(0, len(q1)):
        print "\"" + q1[i][0] + "\" - " + str(q1[i][1]) + " views"
    print("\n")


def question2():
    #Answer to question 2
    print "2. Who are the most popular article authors of all time?"
    q2 = query(question_2)
    for i in range(0, len(q2)):
        print "\"" + q2[i][0] + "\" - " + str(q2[i][1]) + " views"
    print("\n")


def question3():
    #Answer to question 3
    print "3. On which days did more than 1% of requests lead to errors?"
    q3 = query(question_3)
    for i in range(0, len(q3)):
        print str(q3[i][0])+ " - "+str(round(q3[i][3], 2))+"% errors"
    print("\n")


if __name__ == '__main__':
    question1()
    question2()
    question3()
