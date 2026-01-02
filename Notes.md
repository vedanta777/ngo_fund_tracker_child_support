This is a basic walkthrough of the tech kit and know how of what has been used in this project.

Coding Language - Python 
Database Management Software - MySQL
Libraries Required - MySQL Connector 

How the Code works - 

The user enters data after Python provides them with the appropriate prompts after they choose appropriate options (ie, to enter, retrieve, update or manipulate data).
Python then takes the entered data for updation or insertion, or fetches data for retrieval or manipulation. 

Upon running the program, the code establishes a connection between MySQL on your device and Python, for which you need to enter your correct host name, user name and password in the code.
Host name is by default "localhost" for a local device.

Then the code creates the database and all tables if they don't exist. If they do, that line of code is simply ignored.
After that two objects are created - the "connector" for establishing a connection between MySQL and Python, and the "cursor" for interaction between both.

Commit function is used to ensure that any data injection or updation is reflected in the database too. 
Loops are used to create a menu like experience.

What does the code create and do - 

Three tables are created - one for kids of the organisation, one for funds and expenses, and one for workers of the organisation.
A password and a security key (will be added soon) are required for every worker to ensure security of data access.

Limited data retrieval is allowed for normal people and full data is accessible to only workers of the organisation.


