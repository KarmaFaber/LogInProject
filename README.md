# Log In

Log in project in pro and basic version.

## Built With

* [Visual Studio Code](https://code.visualstudio.com/) - Windows 10 version.  
* [Xampp](https://www.apachefriends.org/es/index.html). 

### Project parts
The main difference between the two versions lies in the use of graphic interface and modules to maintain a clean and tidy code.
* log_in_user_basic
* log_in_user_pro_version

### Special modules
* <b>class_sql</b>:
<br/><i>sql</i>=database_host, server_username, server_password, database_name
     - insert_query(sql) -server connection
     - select_query(sql) -mysql queries

### Python libraries used 
* pymysql
* tkinter

### DataBase MySQL
CREATE DATABASE <b>proyect</b>;
<br/>CREATE TABLE <b>user</b> (<b>email</b> varchar (50), <b>password</b> varchar(100), PRIMARY KEY(email));

## Contributing

This project is made for educational purposes, GitHub users are free to download and use it freely.

## Author

* **Karma Faber** 

## Versions:
* <b>version 1.0</b> - Operational Version. Password is entered into the database without encryption and format_checker.
