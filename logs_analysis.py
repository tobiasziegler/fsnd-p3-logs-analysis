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
    results = execute_query(query1)
    for result in results:
        print("- \"%s\" — %s views" % (result[0], result[1]))


def get_top_authors():
    """Find the most popular article authors."""
    query2 = """select name, count(*) as views
                from authors, articles, log
                where authors.id = articles.author
                and log.path like '%' || articles.slug
                group by name
                order by views desc;"""
    results = execute_query(query2)
    for result in results:
        print("- %s — %s views" % (result[0], result[1]))


def get_high_error_days():
    """Find the days on which more than 1%% of requests led to errors."""
    query3 = """select to_char(date, 'Mon dd, yyyy'),
                error_rate from
                    (select a.date, errors, requests,
                    round(100.0 * errors / requests, 1) as error_rate
                    from
                        (select date(time) as date,
                        count(*) as errors
                        from log
                        where status not like '%200%'
                        group by date) as a,
                        (select date(time) as date,
                        count(*) as requests
                        from log
                        group by date) as b
                    where a.date = b.date) as error_rates
                where error_rate >= 1.00;"""
    results = execute_query(query3)
    for result in results:
        print("- %s — %s%% errors" % (result[0], result[1]))


# The main program that performs the analyses when this file is run
if __name__ == '__main__':
    print("1. What are the most popular three articles of all time?")
    get_top_3_articles()
    print("\n2. Who are the most popular article authors of all time?")
    get_top_authors()
    print("\n3. On which days did more than 1% of requests lead to errors?")
    get_high_error_days()
