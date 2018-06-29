# Installing the Lists DB
## Create the database as root/admin
```create database lists;```

## Add a user particular to the database
```CREATE USER user@'localhost' IDENTIFIED BY password;```
## Assign the user privileges for the database
GRANT ALL PRIVILEGES ON lists.* TO user@'localhost';
## Create the tables
Run the code in the ./db/init directory
1. createUsers.sql
2. createLists.sql
3. createTasks.sql
4. createCollaborators.sql

## Create the stored procedures
Presently these are held as individual files, organized by table type in the users, lists, tasks, and collaborators directories.
