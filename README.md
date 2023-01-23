# About F1CoreEngine
A Technion CS Software-Project "F1 Core Engine" for the Autonomous Formula-1 Technion Project

## Data Pipeline Structure
  The data pipline from the car to the gui has 5 main parts:
  1. The Formula Automation Components
  2. Logger
  3. Backend Server
  4. Database
  5. Grafana

## Formula Automation Components
  The formula dispatch server is composed of 3 main components. Each one serves as a Data Source:
    1. Perception: Receives input from different cameras and sensors, and outputs absolute positions
      and information about the surroundings of the car.
    2. State Estimation: Receives the output from the Perception Unit and creates a map
      of the state of the car.
    3. Control: Receives the output of the State Estimation Unit and dictates behaviour
      of the car controls.

  For the purposes of testing, the project also provides a random output generator
  which is meant to simulate each of the components.

## Logger
  The Logger receives output from the Formula Automation Components and
    sends them to the Backend Server.
  The Logger is also in charge of managing the connections and metadata
    about current experiments.
  It is represented as a class, each Formula Automation Component
    addresses the class and logs it's output using it.
  
## Backend Server
  The Backend Server communicates via gRPC with the Logger,
    it receives messages from it, processes them and inserts them into
    the Database tables. It is also in charge of managing open experiment sessions with the Logger.

## Database
  This project uses TimeScaleDB which is an SQL-based database,
  This is since the data processed in this domain heavily relies
    on timing and TimeScaleDB is uniquely optimized for handling this type of data.

## Grafana
  Grafana is a web-based interface for visualizing data.
  It is comprised of a server, and the client (a web browser running client-side javascript).
  The server has multiple dashboards, each functions as it's own page 
  and each dashboard can have have multiple panels to display data streamed from the connected data sources.
  In this project, the grafana server is connected the TimeScaleDB database and displays
  live data & analytics about the car's behaviour.

# Cloning the Project
## Local Dependencies
  * [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
  * [Docker](https://docs.docker.com/get-docker/) - For the purposes of reliability and reproducibility,
    the Backend Server, Database and Grafana Server are meant to be 
    hosted on a docker - each of them as it's own docker image.
    <!-- Python ? -->

## Initial Setup
1. Clone this repository:
> git clone https://github.com/ICST-Technion/F1CoreEngine.git
2. Open docker desktop
3. To initialize the system run the following command within the project directory:
> docker compose up
4. To initialize the database run the following command within the project directory:
> python3 server/db/init_db.py -i
5. Login to grafana in `localhost:3000` with the credentials `admin:admin` (and if you want you can change the password)
6. Add a data source:
   1. Go to the `settings/datasources` screen: # TODO: need to add image
   2. Click `Add data source` button.
   3. Search `postgres` in the search bar:  # TODO: need to add image
   4. Fill the information as shown:
      Host: `database:5432`, Database: `postgres`, User: `postgres`, Password: `password`
   5. Disable SSL
   6. Choose `PostgreSQL` version 15 and switch to `TimescaleDB`
   7. Click `Save & Test`
7. [Import a Dashboard](#Importing-Existing-Dashboards) as per the following instructions.


### Importing Existing Dashboards
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
  1. \\! pg_restore -Fc -d \<DB\> filename.bak
* Run timescaledb_post_restore to return your database to normal operations:
  1. SELECT timescaledb_post_restore();
* Optinal - Reindex your database to improve query performance:
  1. REINDEX DATABASE \<DB\>;
