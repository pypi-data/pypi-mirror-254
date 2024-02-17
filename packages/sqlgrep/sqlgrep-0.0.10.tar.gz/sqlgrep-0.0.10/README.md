# SQLGrep: Grep in MySQL database tables / fields

*If you do not know db schema (drank a lot yesterday, first day on new project or hacking alien starhip database)*

SQLGrep will examine db schema and search (`SELECT ... WHERE ...`) for specified text/number/regex/like (needle) in all fields of all tables.

## Install

To install mysql version on debian you may need to:
~~~
apt install pkg-config libmariadb-dev
~~~

Installation:
~~~
# new way, use pipx if you can (with mysql packages)
pipx install sqlgrep[mysql]

# old-fashioned way  (and postgresql support)
pip install sqlgrep[postgresql]
~~~


## Examples
I use test db with just one table, so all found records will be in "libro" table.

~~~shell
# We want to know where year is stored and we know, at least one book published in 1991
# found in table libro, fields: masterid, id, anno, peso
$ sqlgrep mysql://localhost/libro --limit 1 1991
libro(id=1991) masterId: 1991
libro(id=1991) id: 1991
libro(id=80) anno: '1991'
libro(id=169601) peso: 1991

# LIKE search, I'm only interested in mice...
$ sqlgrep mysql://localhost/libro --like %mice%
libro(id=149894) autore: 'Primicerj Giulio'
libro(id=37004) title: 'ECONOMICESKAIA GHEOGRAFIA SSSR. - Lialikov H.I. - 1961'
libro(id=1359) titolo: 'STUDI MICENEI ED EGEO-ANATOLICI. Fascicolo ottavo.'
libro(id=1367) titolo: 'IL TORO DI MINOSSE. Creta, il Minotauro e la civiltà micenea.'
~~~

## Speed
sqlgrep does one SQL SELECT ... WHERE query for each field in database. So, for db of 5 tables and 10 fields in each, there will be 50 queries (sending query to db is very simple and fast operation). All filtering are performed on database side (not in our slow python code), so it goes with maximal speed.

## Database credentials
Specify database as SQLAlchemy URL like `mysql://user:password@host/db_name` (or `postgresql://...`)

## Usage
~~~
usage: sqlgrep [-h] [--host HOST] [-t TABLES [TABLES ...]] [--like] [--float] [--int] [--limit N] [-c] [--all]
               DB URL needle

database search (SQL grep), version: 0.0.6

positional arguments:
  DB URL                example: mysql://user:password@host/db_name
  needle

options:
  -h, --help            show this help message and exit
  --host HOST
  -t TABLES [TABLES ...], --tables TABLES [TABLES ...]
                        tables (default: all)
  --like                use SQL LIKE instead of =

Types (default - string):
  --float               coerce to float
  --int                 coerce to integer

Output:
  --limit N             Limit to N results for each column
  -c, --count           Count only
  --all                 display ALL fields from matching rows
~~~