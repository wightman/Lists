# Lists DB Documentation
## Procedures for the ```users``` table
---
- `addUser(name, email, passwd, admin)`
  - add a record to the user table.
  - Example
  ```
CALL addUser('You', 'you@unb.ca','$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a', true);
```
- `delUser(userId)`
  - Delete a user.
  - Removes all associated lists, tasks and collaborations
  - Example
  ```
CALL delUser(22);
```
- `getUserNames()`
  - return a table of usernames
  - Example
  ```
CALL getUserNames();
```
- `loginUser(userEmail, password)`
  - confirm login credentials
  - Example
  ```
    CALL loginUser('you@unb.ca', '$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a');
  ```
- `putUser(userId, userName, userEmail, userAdmin)`
  - replace values for an existing user.
  - Example
  ```
  putUser(22, 'Me', me@unb.ca, true);
  ```
- `putUserPassword(userId, password)`
  - set the password for the user.
  - Example
  ```
    putUserPassword(22, '$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPXXhAc1h5teetXv2lsdI77P3q.5a')
    ```
---
## Procedures for the ```lists``` table
- `addList(userId, list)`
  - add a record to the list table for the given user.  


- `getList(userId, list)`
  - return the list name and listId for a user's list record.


- `putUser(user, password, administrate)`
  - return a complete user record for the user.


- `delList(user, list)`
  - delete the user's list from the list table and the associated tasks as well.


- `getUserLists(user)`
  - return the list and listId from a user's list records.



- `addTask(user, list, task, completed)`
  - add a task to a user's list


- `getTasks(user, list)`
  - return the set of tasks for a user's list.


- `putTask(taskId, task, completed)`
  - update a task.


- `delTask(taskId)`
  - delete a specific task via it's ID.
