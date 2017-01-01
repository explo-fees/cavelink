## How to use this sample? ##

This small piece of code explains how to use the module to store data in a SQLite database.

Ensure the store-in-database.py can use the library (put it in the same folder), and run :
    python store-in-database.py

You will get a cavelink.db file in the same folder, with 2 tables.
To consult the content, you can :

    # install sqlite3
    apt-get install sqlite3
    sqlite3

Then, in the prompt, enter the following commands:

    .open cavelink.db
    .mode column on
    .headers on
    select * from data, sensors where sensors.Id = data.sensorId;

## File Description ##

* schema.sql : the SQL script used to initialize the database structure
* store-in-database.py : the script to gather data and store them

## Some explanations ##
You can imagine to schedule the script (using cron). In this case, you could have many duplicates in the database.
SQLite provides a SQL statement "INSERT OR IGNORE INTO <table>" . This is interesting to avoid duplicates. If a record is already there, it will not be imported.

