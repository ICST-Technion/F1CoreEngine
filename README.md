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
