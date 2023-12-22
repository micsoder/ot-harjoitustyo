## Program Architecture

### Build
The build of the program looks currently like this, a three-tier monolithic architecture. 

![Architecture](pictures/achitecture.png)

- *UI* is the graphical user interface
- *logic* is the logic of the program 
- *database* is where the data is saved. 
#### Program logic

![Architecture](pictures/ui_and_logic_architecture.png)

### Sqlite3 Database

All information in the program is saved into a Sqlite3 database in three different tables: 

**1. Users**
The user table holds all information about the user, such as its username, password and admin status. The creation of the database and tables happens in the **database** folder and all handling with the tables, happens in the **logic** folder with specific classes for each table. 

| username |   password    | admin  |
|:---------|:---------|:---------|
|Gandalf|123|1|

**2. zone_base_data**
The zone_base_data holds all information about what is displayed on the map.

| id |   zone_title    | zone_description  | zone_image |
|:---------|:---------|:---------| :---------|
|1|Marisong|A costal land in the....| Marisong.png |

**3. map_page**
Hodl information about the parent map page of each zone so that the go back function always goes back to the parent map.

| map_id |   zone_id    |
|:---------|:---------|
|1|2|
|1|3|
|2|4|

### Architecture of basic functionalities

Below are a couple of sequence diagrams of the login and signup functionalities.  

#### Login architecture

The login functionality works as follows: when the user presses the login button after the user has added the username and password, the following sequences happen. 

- It calls for the login method in the UserHandler class 
- It checks whether the username exists and if the username exists, it returns True, otherwise False
- Then it validates the password to see if it matches the one in the table and returns True if it does match, otherwise False
- It defines the self.current_user in the login method in the UserHandler class
- It return a tuple of the success and a message
- It return back to the user a messagebox which shows if the login was successful or not. 

![Architecture](pictures/login_architecture.png)




#### Signup architecture

The signup functionality works as follows: when the user presses the create account button after the user has added the username and password, the following sequences happen. 

- It calls for the create_account method in the UserHandler class 
- It checks whether the username exists and if the username exists, it returns True, otherwise False
- It check whether the length of the password is longer than three (just to showcase the functioanlity) and returns True, otherwise False.
- Then it hashes the password
- It creates a new account by adding the username, password and admin status to the table and return True if it was succesful, otherwise False. 
- It returns a tuple of the success and a message
- It returns back to the user a messagebox which shows if the account creation was successful or not. 

![Architecture](pictures/signup_architecture.png)
