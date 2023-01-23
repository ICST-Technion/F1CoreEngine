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
`git clone https://github.com/ICST-Technion/F1CoreEngine.git`
2. Open docker desktop
3. To initialize the system run the following command within the project directory:
`docker compose up`
4. To initialize the database run the following command within the project directory:
`python3 server/db/init_db.py -i`
5. Login to grafana in `localhost:3000` with the credentials `admin:admin` (and if you want you can change the password)
6. Add a data source:
   1. Go to the `settings > datasources` screen: <img width="1786" alt="image" src="https://user-images.githubusercontent.com/63338501/214157577-48e001cd-f433-4b7b-a16a-c3db5f22d441.png">
   2. Click `Add data source` button.
   3. Search `postgres` in the search bar:  <img width="1780" alt="image" src="https://user-images.githubusercontent.com/63338501/214157678-09ac98c5-2abd-449c-b499-ab624219a578.png">
   4. Fill the information as shown: 
      1. Host: `database:5432`, Database: `postgres`, User: `postgres`, Password: `password`
      2. Disable SSL
      3. Choose `PostgreSQL` version 15 and switch to `TimescaleDB`
      4. Click `Save & Test`<img width="1116" alt="image" src="https://user-images.githubusercontent.com/63338501/214158110-471b8c1b-f763-4e0a-b0fe-3bd1e5ab07df.png">

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

# Using the logger to send messages:
The logger is a python class with the following class methods that should be used in the following order:
* `Connect` - Initialize a connection with the System.
* `NewExperiment` - Declares that the following messages will be send from a new experiment.
* Use `Logger.log(<proto message containing the data of type Message>)`
* `EndExperiment` - Declares that the experiment has ended.

# Backing up your Database to .bak file

In order to backup the database from the docker container:
*. `pg_dump -U postgres -Fc -f <file_name>.bak postgres`

To backup the database from the host machine:
*. `pg_dump -h localhost -p 5432 -U postgres -Fc -f <file_name>.bak postgres`

# Loading Data from .bak file
* Before Loading the backup file, run the following command (this command will delete all the data on the database, so if you need it it's a good time to [backup](#Backing-up-your-Database-to-bak-file):
`python3 server/db/init_db.py -d`

Assuming you have a .bak backup file, this are the steps to do in order to load and use the data in the file:
1. Connect to the database, `psql -h localhost -p 5432 -U postgres -d postgres`.
2. Run timescaledb_pre_restore to put your database in the right state for restoring:
  `SELECT timescaledb_pre_restore()`; 
3. Restore the database:
  `\! pg_restore -Fc -d postgres <path_to_file>.bak`
4. Run timescaledb_post_restore to return your database to normal operations:
  `SELECT timescaledb_post_restore();`
5. Optinal - Reindex your database to improve query performance:
  `REINDEX DATABASE \<DB\>;`

# Clearing the database (without dropping the tables):
`python3 server/db/init_db.py -c`
