# LearnSomeSQL
A mock database that can be used to learn some SQL.

The database is a sqlite3 database. It can be queried using the command line or using a .sql file. I recommend the latter for the sake of learning how to write good SQL queries. The database has many countries and cities and 10 synthetic KPIs to go with each key. When the country is the US, there is an additional populated column for the state.  The KPIs have some random outliers and missing data. The generation of the database can be seen in database.py and countries_cities.py.

In order to run a query from a file, first write the query and save it as query.sql (or whatever). Then from the command line, use "sqlite3 synthetic_cities_kpi.db < query.sql"  The result of query will print in the terminal (or any errors).  Experiment.
