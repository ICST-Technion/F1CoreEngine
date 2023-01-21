# F1CoreEngine
A Technion CS Software-Project "F1 Core Engine" for the Autonomous Formula-1 Technion Project

In order to backup your database, you can use this command:
1. pg_dump -Fc -f filename.bak database_name

To backup a database named tsdb hosted on a remote server use:
1. pg_dump -h <REMOTE_HOST> -p 55555 -U tsdbadmin -Fc -f tsdb.bak tsdb

Assuming you have a .bak backup file, this are the steps to do in order to load and use the data in the file:
* In psql, create a new database to restore to, and connect to it:
  1. CREATE DATABASE tsdb;
  2. \c tsdb
  3. CREATE EXTENSION IF NOT EXISTS timescaledb;
* Run timescaledb_pre_restore to put your database in the right state for restoring:
  1. SELECT timescaledb_pre_restore();
* Restore the database:
  1. \! pg_restore -Fc -d tsdb tsdb.bak
* Run timescaledb_post_restore to return your database to normal operations:
  1. SELECT timescaledb_post_restore();
* Optinal - Reindex your database to improve query performance:
  1. REINDEX DATABASE tsdb;
