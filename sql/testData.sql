-- build some users
INSERT INTO users (userName, userEmail, userPassword, userAdmin)
   VALUES('Me', 'me@unb.ca','$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a', true);
CALL addUser('You', 'you@unb.ca','$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a', true);

CALL getUser(1);
CALL getUserNames(); -- need to create
-- build a list
CALL addList(1, 'Stuff');
CALL addList(2, 'INFO1103');

CALL getList(2);

-- build some tasks
CALL addTask(1, 'Haircut',2,false);
CALL addTask(2, 'Finish Assignment 3',1,false);
CALL addTask(2, 'Finish Lab 5',1,false);

-- what needs to be done?
CALL getListTasks(2);

-- Make me a collaborator on your list
CALL addCollaborator(1,2,'R');

-- List collaborators, access for a listName
CALL listCollaborators(2)
