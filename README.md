# LearnSomeSQL
I remember when I learned SQL that I hated all the online resources I was finding.  All the "databases" were really small, super clean and the challenges presented were really easy.  I don't think I ever really learned SQL until I had a job with a large database with lots of tables, complicated questions and all the things that go with live data. So with that in mind, I created a mock database that can be used to learn some SQL slightly more realistically.

The database itself is too large for github, so you'll have to run database.py locally in order to build your own copy of it.

The database is a sqlite3 database. It can be queried using the command line or using a .sql file. I recommend the latter for the sake of learning how to write good SQL queries. The database has many countries and cities and 10 synthetic KPIs to go with each key. When the country is the US, there is an additional populated column for the state.  The KPIs have some random outliers and missing data. The generation of the database can be seen in database.py and countries_cities.py.

In order to run a query from a file, first write the query and save it as query.sql (or whatever). Then from the command line, use "sqlite3 synthetic_cities_kpi.db < query.sql"  The result of query will print in the terminal (or any errors).  I'm not going to pretend to know all the possible variations across different operation systems and whatnot. I ran this initially on a Mac with Python 3.12. Experiment.


# How to use this repo
The trick here is to come up with some questions that you want to try to answer, and then mess around with the SQL until you get it.  At least, that's how I learned.  In order to even ask meaningful questions, you'll have to use some SQL commands to learn about the database in the first place. How will you verify if your answers are correct? You aren't going to break anything here, so have some fun with it.  Maybe you can create another table and add it to the database yourself? The sky is the limit.

For an example, I included a query that answers the question "Over the entire time period covered in the database and for countries that start with S, what is the mean value of kpi_4 and kpi_6 and how many times did the leaders change?" 
