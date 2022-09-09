# ----- Example Python program to create a database in PostgreSQL using Psycopg2 -----

# import the PostgreSQL client for Python

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connect to PostgreSQL DBMS
con = psycopg2.connect("user=postgres password='root'");
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);

# Obtain a DB Cursor
cursor          = con.cursor();
name_Database   = "SocialMedia";

 

# Create table statement
sqlCreateDatabase = "create database "+name_Database+";"

# Create a table in PostgreSQL database
cursor.execute(sqlCreateDatabase);