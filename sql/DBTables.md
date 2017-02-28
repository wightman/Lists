# Lists DB Documentation

## Tables

### users
- User records
- userName is effectively display names
- userEmail is the login userName
- userPassword is a Bcrypted hash
- Admin indicates ability to perform admin functions.
```sql
    userId INT NOT NULL AUTO_INCREMENT,
    userName VARCHAR(255) NOT NULL,
    userEmail VARCHAR(255) UNIQUE NOT NULL,
    userPassword BINARY(60) NOT NULL,
    userAdmin BOOLEAN NOT NULL DEFAULT 0,
    userSince TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

   PRIMARY KEY (userId)
```

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
- Task records that make up a list.
- Tasks have a unique ID and belong to a single list.
- Tasks have a position/priority. Duplicate values can exist within a list
- Tasks need not have unique descriptions (task).
- Tasks are denoted with the userID of their creator (collaboratorID)
- Tasks disappear when lists are deleted.
```sql

  taskId INT NOT NULL AUTO_INCREMENT,
  taskPosition INT NOT NULL DEFAULT 1,
  task VARCHAR(255),
  completed BOOLEAN DEFAULT false,
  listId INT NOT NULL,
  collaboratorID INT NOT NULL,
  taskSince  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  PRIMARY KEY (taskId),
  FOREIGN KEY (listId)
        REFERENCES lists(listId)
        ON DELETE CASCADE
```

### collaborators
- Collaborators on lists
- Collaborators disappear when lists are deleted.
- Value in access column *must* be present in the accessType table
```sql
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
```

### accessTypes
- List of types of access for collaborators
- Used to work-around mySQL not supporting CHECK IN constraints
```sql
  access CHAR(1) UNIQUE
```
