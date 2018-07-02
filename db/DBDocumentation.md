# Lists DB Documentation
The procedures and table definitions for the Lists database, organized according to the Story docuemnt in the main Lists directory.
## Stored Procedures
Stored procedures are organized primarily by the table/theme they most pertain to: users, lists, items and collaborators.
### ```users``` table
- `addUser(name, email, passwd, admin)`
  - add a record to the user table.
  - name and email are strings
  - password is a BINARY(60) bcrypt hash of the password
  - Example
  ```sql
  CALL addUser(
    'You',
    'you@example.ca',
    '$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a'
    , true);
```
  - on error: `ERROR 1644 (52711): Unable to add the user.`


- `delUser(userId)`
  - Delete a user
  - Doesn't care if user doesn't exist
  - Removes all associated lists, items and collaborations
  - Example
  ```sql
  CALL delUser(22);
```
  - on error: `ERROR 1644 (52710): User not found.`


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
  - on error: `ERROR 1644 (52710): User not found.`


- `putUserAdmin(userId, admin)`
  - set the administration flag for a user (true or false)
  - on error: `ERROR 1644 (52710): User not found.`
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
  - on error: `ERROR 1644 (52710): User not found.`


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
  - on error: `ERROR 1644 (52721): Unable to create the list.'


- `delList(listID)`
  - remove a list
  - also removes corresponding item items and collaborators
  - Example
  ```sql
    CALL delList(2);
    ```
  - on error: `ERROR 1644 (52720): List not found.

- `getList(listId)`
  - return the list record for a listId. *Note this does not return the set of items for the list.*
  - Example
  ```sql
    CALL getList(1);
    ```
    - on error: `ERROR 1644 (52720): List not found.

- `getUserLists(userId)`
  - return the list name and listId for a user's list record.
  - Example
  ```sql
    CALL getUserLists(2);
    ```
  - on error: `ERROR 1644 (52710): User not found.`


- `putList(listID, listName, listDescription)`
  - update information for a list.
  - Example
  ```sql
    CALL putList(2,"INFO1103","Stuff I should have done.");
    ```
  - on error: `ERROR 1644 (52710): User not found.`

### ```items``` table

- `addItem(listID, itemName, itemDescription, itemPos, creatorID, completed)`
  - add a item to a list
  - Example
  ```sql
  CALL addItem(1, 'Haircut','Shorter, please',2, 1,false);
    ```
  - on error: `ERROR 1644 (52731): Unable to create the item.`


- `delItem(itemId)`
  - delete a item
  ```sql
  CALL delItem(3);
    ```
  - on error: `ERROR 1644 (52730): item not found.`


- `getListItems(listId)`
  - return the set of items for a user's list.
  ```sql
  CALL getListItems(1);
    ```
    - on error: `ERROR 1644 (52720): List not found.


- `putItem(itemId, itemName, itemDetail, iPos, completed)`
  - update a item.
  ```sql
  CALL putItem(1, 'Hair tonic', 'please grow!',1,false);
    ```
  - on error: `ERROR 1644 (52730): item not found.`

  ### ```collaborators``` table

- `addCollaborator(userId, listId, access)`
  - give a user access to a list
  ```sql
  CALL addCollaborator(2,1,'R');
  ```
  - on error: `ERROR 1644 (52742): List owner cannot be a collaborator.`
  - on error: `ERROR 1644 (52741): Unable to create the collaboration.`


- `delCollaborator(userId, listId)`
  - remove user access to a list
  ```sql
  CALL delCollaborator(2,1);
  ```
  - on error: `ERROR 1644 (52740): Collaboration not found.`


- `getCollaborators(listId)`
  - get users and their access types to a list
  ```sql
  CALL delCollaborator(1);
  ```
  - on error: `ERROR 1644 (52720): list not found.`


- `putCollaborator(userId, listId, access)`
  - modify user access to a list
  ```sql
  CALL putCollaborator(2,1,'W');
  ```
  - on error: `ERROR 1644 (52740): Collaboration not found.`


- `getAccessTypes();`
  - get the permitted accessType values
  ```sql
  CALL getAccessTypes();
  ```

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

### items
- item records make up a list.
- items have a unique ID and belong to a single list.
- items have a position/priority. Duplicate values can exist within a list
- items need not have unique descriptions (item).
- items are denoted with the userID of their creator (list owner or collaborator)
- items disappear when lists are deleted.
````sql
itemId INT NOT NULL AUTO_INCREMENT,
itemPosition INT NOT NULL DEFAULT 1,
itemName VARCHAR(255),
itemDetail VARCHAR(255),
completed BOOLEAN DEFAULT false,
listId INT NOT NULL,
creatorId INT NOT NULL,
itemSince  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

PRIMARY KEY (itemId),
FOREIGN KEY (listId)
        REFERENCES lists(listId)
        ON DELETE CASCADE
````

### collaborators
- Collaborators on lists
- Collaborators (not the user) disappear when lists are deleted.
- Value in access column *must* be present in the accessType table
- A user can collaborate once on a list (multiple records not allowed)
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
  REFERENCES accessTypes(access),
UNIQUE KEY collaboratorList (userId, listId)
````

### accessTypes
- List of types of access for collaborators
- Used to work-around mySQL not supporting CHECK IN constraints, but it turns
out that being able to list the valid domain of values is useful.
- Really, the table is populated with three constants: 'O', 'R'
 and 'W', so there is no need for write access to the table.
 ````sql
  access CHAR(1) UNIQUE
````
