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
<br/><i>#sql</i>=database_host, server_username, server_password, database_name
     - insert_query(sql) -server connection
     - select_query(sql) -mysql queries

* <b>encrypt</b> -password encryption:
     - encrypt_password_shamd5(password)
     

### Python libraries used 
* pillow
* pymysql (vers: 0.9.3)
* random
* string
* tkinter

### DataBase MySQL
CREATE DATABASE <b>proyect</b>;
<br/>CREATE TABLE <b>user</b> (<b>email</b> varchar (50), <b>password</b> varchar(100), PRIMARY KEY(email));

## Contributing

* Check the open issues or open a new issue to start a discussion around your feature idea or the bug you found. 
* Fork the repository, make your changes, and add yourself to AUTHORS.md
* Send a pull request

## Author

* [Karma Faber](https://www.linkedin.com/in/maria-zolotarova/). 

## Versions
* <b>version 1.0</b> - Operational Version. Password is entered into the database without encryption and format_checker.
* <b>version 1.2</b> - Operation Version.
  - encrypt module - fixed

## License

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of this software dedicate any and all copyright interest in the software to the public domain. We make this dedication for the benefit of the public at large and to the detriment of our heirs and successors. We intend this dedication to be an overt act of relinquishment in perpetuity of all present and future rights to this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
  
