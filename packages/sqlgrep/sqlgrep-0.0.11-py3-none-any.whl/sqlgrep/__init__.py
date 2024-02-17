#!/usr/bin/env python3

import argparse
import os
import sys

from rich import print as rprint
from rich.progress import track

from sqlalchemy import create_engine, inspect, or_, cast, String, Integer, Float
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy as sa


__version__='0.0.11'

def get_args():


    parser = argparse.ArgumentParser(description='database search (SQL grep), version: {}'.format(__version__))
  
    parser.add_argument('db', metavar='DB URL', default=None, help='example: mysql://user:password@host/db_name')

    parser.add_argument('--host', default=os.getenv('MYSQL_HOST','localhost'))
    parser.add_argument('-t', '--tables', nargs='+', default=list(), help="tables (default: all)")
    parser.add_argument('--like', default=False, action='store_true', help="use SQL LIKE instead of =")

    g = parser.add_argument_group('Types (default - string)')
    g.add_argument('--float', default=False, action='store_true', help='coerce to float')
    g.add_argument('--int', default=False, action='store_true', help='coerce to integer')

    g = parser.add_argument_group('Output')
    g.add_argument('--limit', metavar='N', type=int, help='Limit to N results for each column')
    g.add_argument('-c', '--count', default=False, action='store_true', help='Count only')
    g.add_argument('--all', default=False, action='store_true', help="display ALL fields from matching rows")


    parser.add_argument('needle')


    return parser.parse_args()

        
def search_column(session, table, column, needle):
    # Define a list to hold all the conditions for each field
    
    inspector = inspect(table)
    pk_name = inspector.primary_key[0].key

    if args.like:
        condition = column.like(needle)
    elif args.int:
        condition = cast(column, Integer) == needle
    elif args.float:
        condition = cast(column, Float) == needle
    else:
        condition = cast(column, String) == needle

        
    # Use the final condition in a select query
    query = session.query(table).filter(condition)

    if args.limit:
        query = query.limit(args.limit)

    if args.count:
        count = query.count()
        if count:
            print(f"{column}: {count} rows matched")
        return
    
    try:
        result = query.all()
    except (Exception, TypeError) as e:
        print(f"EXCEPTION: {type(e)} in {table.__table__.name}/{column}")
        return

    # Print the results
    for row in result:
        value = getattr(row, column.key)
        if args.all:
            rprint(row.__dict__)
        else:
            print(f"{column.table}({pk_name}={getattr(row, pk_name)}) {column.name}: {value!r}")

def main():
    global args

    args = get_args()

    tables = args.tables
    needle = args.needle
    limit = args.limit

    engine = create_engine(args.db)
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    # session = Session(engine)
    conditions = []


    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Iterate through all tables and their fields
    for table_name, table in Base.classes.items():
        if args.tables and table_name not in args.tables:
            continue
        for column in track(table.__table__.columns, transient=True, description=table_name):
            search_column(session, table, column, needle)


if __name__ == '__main__':
    main()