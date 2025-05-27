# DIS-Project

## Project in the "Databases and Informations" course at University of Copenhagen, 2025. 

Made by Thomas T. Olsen, Thomas F. Lund and Rasmus D. Kristensen

## How to run the web-app: 

To run and compile the project, first make sure that you have Docker installed.

Open Docker, then clone or download this repository. 

Open your terminal, and navigate to the project folder. 

Write the following command: 

```
docker-compose up --build
```

Open a browser window and copy and paste the following: 

```
http://localhost:5001/
```

You now have access to our web app! 


In order to shut down the web app, press 

```
control + c
```

in your terminal. 

To clean up temporary Docker files, write

```
docker compose down -v
```

## How to interact with the web-app: 

Our app is called "Bike Buddy" and is intended for people who are into cycling and are tired of cycling alone. The user is able to find others in their own or other postal codes to match their skill level (beginner, intermediate, advanced). 

The web app consists of two pages, "index" and "signup". 

In index, you are able to browse through all users and select specific combinations of postal codes and skill levels of users. 

In signup, you may sign up as a new user of the app with credentials username, email, postal code and skill level. User id is unique and assignmed internally upon signup. 