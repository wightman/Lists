# Installing the Lists DB
## Create the database as root/admin
```sql
CREATE database lists;
```

## Add a user particular to the database with admin privileges

```sql
CREATE USER user@'localhost' IDENTIFIED BY password;
GRANT ALL PRIVILEGES ON lists.* TO user@'localhost';
```

## Create the tables
Run the code in the ./db/init directory (in this order)
1. createUsers.sql
2. createLists.sql
3. createItems.sql
4. createCollaborators.sql (also creates the accessTypes table and its records: O, R, W)

## Create the stored procedures
Presently these are held as individual files, organized by table type in the users, lists, items, and collaborators directories.
+ the stored procedures for collaborations should be created before the items stored procedures.
