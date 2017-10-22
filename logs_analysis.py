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
