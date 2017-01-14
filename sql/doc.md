# Lists DB Documentation

## Tables

### users
- User table. Admin indicates ability to perform admin functions.
````sql
   userId       INT          NOT NULL AUTO_INCREMENT,
   userName     VARCHAR(255) UNIQUE NOT NULL,
   userPassword VARCHAR(255) NOT NULL,
   userAdmin    BOOLEAN      DEFAULT false,
   PRIMARY KEY (userId)
````
### lists
- Task list table. Lists have a unique ID and belong to a user. List names must be unique to a user.
````sql
   listId   INT          NOT NULL AUTO_INCREMENT,
   listName VARCHAR(255) NOT NULL,
   userId   INT          NOT NULL,

   PRIMARY KEY (listId),
   FOREIGN KEY (userId)
        REFERENCES users(userId)
        ON DELETE CASCADE,
   UNIQUE KEY listIdName ( userId, listName)
````
### tasks
- Task table. Tasks have a unique ID and belong to a single list. Task need no have unique descriptions (task).
````sql
   taskId    INT          NOT NULL AUTO_INCREMENT,
   task      VARCHAR(255),
   completed BOOLEAN      DEFAULT false,
   listId    INT          NOT NULL,

   PRIMARY KEY (taskId),
   FOREIGN KEY (listId)
        REFERENCES lists(listId)
        ON DELETE CASCADE
````
## Functions
- `userName2Id(user)`
  - returns the userId for a given user.
- `listName2Id(user, list)`
  - returns the listId for a given user's list.

## Procedures
### users
- `addUser(user, password, administrate)`
  - add a record to the user table.


- `getUser(user)`
  - return a complete user record for the user.


- `putUserPassword(user, password)`
  - set the password for the user.

- `putUserAdmin(user, admin)`
  - set the password for the user.

- `delUser(user)`
  - delete the user from the user table. This also deletes all lists and tasks associated with this user.


- `getUserNames()`
  - return all user names.

### lists
- `addList(user, list)`
  - add a record to the list table for the given user.


- `getList(user, list)`
  - return the list name and listId for a user's list record.


- `putUser(user, password, administrate)`
  - return a complete user record for the user.


- `delList(user, list)`
  - delete the user's list from the list table and the associated tasks as well.


- `getUserLists(user)`
  - return the list and listId from a user's list records.


### tasks
- `addTask(user, list, task, completed)`
  - add a task to a user's list


- `getTasks(user, list)`
  - return the set of tasks for a user's list.


- `putTask(taskId, task, completed)`
  - update a task.


- `delTask(taskId)`
  - delete a specific task via it's ID.
