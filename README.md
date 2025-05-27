# DIS-Project

## Project in the "Databases and Informations" course at University of Copenhagen, 2025. 

Made by Thomas T. Olsen, Thomas F. Lund and Rasmus D. Kristensen

## How to run the web-app: 

To run and compile the project, first make sure that you have Docker installed and working.

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

## How to interact with the web app: 

Our app is called "Bike Buddy" and is intended for people who are into cycling and are tired of cycling alone. The user is able to find others in their own or other postal codes to match their skill level (beginner, intermediate, advanced). 

The web app consists of two pages, "index" and "signup". 

In index, you are able to browse through all users and select specific combinations of postal codes and skill levels of users. 

In signup, you may sign up as a new user of the app with the credentials username, email, postal code and skill level. User id is unique (primary key) and is assigned internally upon signup. 


## Project Requirements

E/R diagram is available in this repository. 

Regular expressions: 

We used the following expression to make sure that a postal code is a 4-digit number (see app.py): 

```
postal_pattern = re.compile(r"^\d{4}$")
```

SQL: 

We used the following queries to extract and/or select relevant information from the database (see app.py): 

```
SELECT username, id, email, skill_level, postal_code
FROM users
WHERE TRUE
```

```
INSERT INTO users (username, email, skill_level, postal_code)
VALUES (%s, %s, %s, %s)
```
