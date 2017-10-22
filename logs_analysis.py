#!/usr/bin/env python3

import psycopg2

def execute_query(query):
    """Connect to the database, execute the specified query and return the
    results."""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results

def get_top_3_articles():
    """Find the most popular three articles of all time."""
    query1 = """select title, count(*) as views
                from articles, log
                where log.path like '%' || articles.slug
                group by title
                order by views desc
                limit 3;"""
    return execute_query(query1)

def get_top_authors():
    """Find the most popular article authors."""
    query2 = """select name, count(*) as views
                from authors, articles, log
                where authors.id = articles.author
                and log.path like '%' || articles.slug
                group by name
                order by views desc;"""
    return execute_query(query2)

def get_high_error_days():
    """Find the days on which more than 1%% of requests led to errors."""
    query3 = """select date, error_rate from
                    (select a.date, errors, requests,
                    round(100.0 * errors / requests, 2) as error_rate
                    from
                        (select date_trunc('day', time) as date,
                        count(*) as errors
                        from log
                        where status not like '%200%'
                        group by date) as a,
                        (select date_trunc('day', time) as date,
                        count(*) as requests
                        from log
                        group by date) as b
                    where a.date = b.date) as error_rates
                where error_rate >= 1.00;"""
    return execute_query(query3)

# The main program that performs the analyses when this file is run
if __name__ == '__main__':
    print("1. What are the most popular three articles of all time?")
    print(get_top_3_articles())
    print("2. Who are the most popular article authors of all time?")
    print(get_top_authors())
    print("3. On which days did more than 1%% of requests lead to errors?")
    print(get_high_error_days())
