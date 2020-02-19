# ETL-Service requirements

Your mission (if you wish to accept) will be to create an ETL service in python to transfer data from a production database to another data warehouse.

Attached you can find 2 CSV files (users and orders).  These files simulate the production database data. Download the CSV files and insert them into a local database of your choice (for example MongoDB).

Create a python service with cron job that runs every 5 min (preferably using flask with flask cron).
The purpose of this cron job is to extract updated orders records (along with their user information) from the production database and push them into the data warehouse (Postgres DB) into 1 table.

Imagine that today is January 1th, 2020.
You need to quickly synchronize all previous orders before today and after this day use the cron job to synchronize new orders.
You will need to simulate the clock moving forward by 5 min every time the cron job starts to work. 
So time on the first run of cron job will be 01/01/2020 00:00
And next time cron job runs it will be 01/01/2020 00:05 and so on.

Note that the updated_at column holds the date and time of the last update of a record.

All code should be on http://github.com and should be easy to install for the developer