# F1CoreEngine
A Technion CS Software-Project "F1 Core Engine" for the Autonomous Formula-1 Technion Project

# Initializing the Grafana Server
In this section we will go over how to reproduce the Grafana Server on new systems
that have cloned this project. In the section we assume the following has already been done:
* This project's repository has been cloned on the local machine. 
* An empty Grafana Server has been set up.

1. Open the we browser of your choice.
2. Insert the URL of the running Grafana Server.
3. Login to the server with an admin account.
4. Click Dashboards > Browse ![image](https://user-images.githubusercontent.com/62563844/212919902-6475ecf9-a7cb-4698-aa92-495637d25b4a.png)
5. Click New > Import ![image](https://user-images.githubusercontent.com/62563844/212920167-79e7b251-f6f9-49a7-b7c0-b06da67a19bd.png)
6. Navigate to your local clone of this repository, then go to the 'Dashboards' folder and select one of the dashboard '.json' files.
7. This process should be repeated for all dashboard files in that folder.
8. You should now have all of the required dashboards available in your server.

# Backing up your Database to .bak file

In order to backup your database, you can use this command:
1. pg_dump -Fc -f filename.bak postgres

To backup a database hosted on a remote server use:
1. pg_dump -h \<REMOTE_HOST\> -p 5432 -U \<USER\> -Fc -f filename.bak postgres

# Loading Data from .bak file

Assuming you have a .bak backup file, this are the steps to do in order to load and use the data in the file:
* In psql, create a new database to restore to, and connect to it:
  1. CREATE DATABASE \<DB\>;
  2. \c \<DB\>
  3. CREATE EXTENSION IF NOT EXISTS timescaledb;
* Run timescaledb_pre_restore to put your database in the right state for restoring:
  1. SELECT timescaledb_pre_restore();
* Restore the database:
  1. \! pg_restore -Fc -d \<DB\> filename.bak
* Run timescaledb_post_restore to return your database to normal operations:
  1. SELECT timescaledb_post_restore();
* Optinal - Reindex your database to improve query performance:
  1. REINDEX DATABASE \<DB\>;
