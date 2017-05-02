# Lists DB Documentation
The procedures and table definitons for the Lists database.
## Stored Procedures
Stored procedures are organized primarily by the table/theme they most pertain to: users, lists, tasks and collaborators.
### ```users``` table
- `addUser(name, email, passwd, admin)`
  - add a record to the user table.
  - name and email are strings
  - password is a BINARY(60) bcrypt hash of the password
  - Example
  ```sql
CALL addUser('You', 'you@example.ca','$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a', true);
```
  - on error: `ERROR 1644 (52701): Unable to add the user.`


- `delUser(userId)`
  - Delete a user
  - Doesn't care if user doesn't exist
  - Removes all associated lists, tasks and collaborations
  - Example
  ```sql
CALL delUser(22);
```
  - on error: `ERROR 1644 (52702): User not found.`


- `getUserNames()`
  - return a table of usernames
  - Example
  ```sql
CALL getUserNames();
```


- `putUser(userId, userName, userEmail)`
  - replace values for an existing user.
  - Example
  ```sql
  CALL putUser(22, 'Me', 'me@example.ca');
  ```
  - on error: `ERROR 1644 (52702): User not found.`


- `putUserAdmin(userId, admin)`
  - set the administration flag for a user (true or false)
  - on error: `ERROR 1644 (52702): User not found.`
  - Example:
  ```sql
  CALL putUserAdmin(22, true);
  ```

- `putUserPassword(userId, password)`
  - set the password for the user.
  - Example
  ```sql
  CALL putUserPassword(22, '$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPXXhAc1h5teetXv2lsdI77P3q.5a')
    ```
  - on error: `ERROR 1644 (52702): User not found.`


- `verifyUser(userEmail, password)`
  - confirm login credentials
  - Example
  ```sql
    CALL verifyUser('you@example.ca', '$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a');
  ```
  - on error: `ERROR 1644 (52700): Bad credentials.`



###  ```lists``` table

- `addList(userId, listName, listDescription)`
  - add a record to the list table for the given user.  
  - Example
  ```sql
    CALL addList(1,'INFO1103', 'To do before the end of term');
    ```
  - on error: `ERROR 1644 (52703): Unable to create the list.'


- `delList(listID)`
  - remove a list
  - also removes corresponding task items and collaborators
  - Example
  ```sql
    CALL delList(2);
    ```
  - on error: `ERROR 1644 (52704): List not found.

- `getList(listId)`
  - return the list record for a listId. *Note this does not return the set of tasks for the list.*
  - Example
  ```sql
    CALL getList(1);
    ```
    - on error: `ERROR 1644 (52704): List not found.

- `getUserLists(userId)`
  - return the list name and listId for a user's list record.
  - Example
  ```sql
    CALL getUserLists(2);
    ```
  - on error: `ERROR 1644 (52702): User not found.`


- `putList(listID, listName, listDescription)`
  - update information for a list.
  - Example
  ```sql
    CALL putList(2,"INFO1103","Stuff I should have done.");
    ```
  - on error: `ERROR 1644 (52702): User not found.`

### ```tasks``` table

- `addTask(user, list, task, completed)`
  - add a task to a user's list


- `getTasks(user, list)`
  - return the set of tasks for a user's list.


- `putTask(taskId, task, completed)`
  - update a task.


- `delTask(taskId)`
  - delete a specific task via it's ID.

  ### ```collaborators``` table


## Tables

### users
- User records
- userName is effectively display names
- userEmail is the login userName
- userPassword is a Bcrypted hash
- Admin indicates ability to perform admin functions
```sql
    userId INT NOT NULL AUTO_INCREMENT,
    userName VARCHAR(255) NOT NULL,
    userEmail VARCHAR(255) UNIQUE NOT NULL,
    userPassword BINARY(60) NOT NULL,
    userAdmin BOOLEAN NOT NULL DEFAULT 0,
    userSince TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

   PRIMARY KEY (userId)
```
#### Notes
- Time turns out to be difficult thing, especially since there's some lack of agreement on a standard. [This discussion](http://dba.stackexchange.com/questions/20217/mysql-set-utc-time-as-default-timestamp) helped.
- There's still the discussion of what ISO time format to use on the server application side, but at least it's right for the database.
- As an interesting aside on the fragility of our concept of time, check out [@ajlburke](https://twitter.com/ajlburke)'s [4 Weird Things About Time](4 Weird Things About Time), presented at [MaritimeDevCon](https://maritimedevcon.ca/), 2016

### lists
- List records.
- Lists have a unique ID and belong to a user.
- List names must be unique to a user.
- Lists disappear when users are deleted.
````sql
  listId INT NOT NULL AUTO_INCREMENT,
  listName VARCHAR(255) NOT NULL,
  userId INT NOT NULL,
  listSince TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  PRIMARY KEY (listId),
  FOREIGN KEY (userId)
        REFERENCES users(userId)
        ON DELETE CASCADE,
  UNIQUE KEY listIdName ( userId, listName)
````

### tasks
- Task records make up a list.
- Tasks have a unique ID and belong to a single list.
- Tasks have a position/priority. Duplicate values can exist within a list
- Tasks need not have unique descriptions (task).
- Tasks are denoted with the userID of their creator (list owner or collaborator)
- Tasks disappear when lists are deleted.
````sql
taskId INT NOT NULL AUTO_INCREMENT,
taskPosition INT NOT NULL DEFAULT 1,
taskName VARCHAR(255),
taskDescription VARCHAR(255),
completed BOOLEAN DEFAULT false,
listId INT NOT NULL,
creatorId INT NOT NULL,
taskSince  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  PRIMARY KEY (taskId),
  FOREIGN KEY (listId)
        REFERENCES lists(listId)
        ON DELETE CASCADE
````

### collaborators
- Collaborators on lists
- Collaborators (not the user) disappear when lists are deleted.
- Value in access column *must* be present in the accessType table
````sql
  userId INT NOT NULL,
  listId INT NOT NULL,
  access CHAR(1) NOT NULL,
  collaboratorSince TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  FOREIGN KEY (userId)
    REFERENCES users(userId)
    ON DELETE CASCADE,
  FOREIGN KEY (listId)
    REFERENCES lists(listId)
    ON DELETE CASCADE,
  FOREIGN KEY (access)
    REFERENCES accessTypes(access)
````

### accessTypes
- List of types of access for collaborators
- Used to work-around mySQL not supporting CHECK IN constraints
- Really, the table is populated with two constants: 'R'
 and 'W', so there is no need for write access to the table, ever.
 ````sql
  access CHAR(1) UNIQUE
````
