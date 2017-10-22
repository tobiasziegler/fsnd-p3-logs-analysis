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

# The main program that performs the analyses when this file is run
if __name__ == '__main__':
    print("1. What are the most popular three articles of all time?")
    print("2. Who are the most popular article authors of all time?")
    print("3. On which days did more than 1%% of requests lead to errors?")
