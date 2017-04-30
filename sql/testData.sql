-- build some users
-- INSERT INTO users (userName, userEmail, userPassword, userAdmin) VALUES('Me', 'me@unb.ca','$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a', true);
CALL addUser('You', 'you@example.ca','$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a', true);
CALL addUser('Me', 'me@example.ca','$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a', true);
CALL addUser('Them', 'them@example.ca','$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a', true);

CALL delUser(3);
-- should break
CALL delUser(1000);

CALL getUser(1);
-- should break
CALL getUser(1000);

CALL getUserNames();
CALL getUsersAll();

CALL verifyUser('me@example.ca','$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a');
-- should break
CALL verifyUser('me@example.ca','$FAIL0$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a');

CALL putUser(1, 'You', 'TheNewYou@example.ca');
-- should break
CALL putUser(1000, 'You', 'TheNewYou@example.ca');

CALL putUserPassword(1,'$FAIL0$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a');
-- should break
CALL putUserPassword(1000,'$FAIL0$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a');

CALL setUserAdmin(1, false);
-- should break
CALL setUserAdmin(1000, false);

-- All user table procedures work!

-- build a list
CALL addList(1, 'Stuff', NULL);
CALL addList(2, 'INFO1103', 'What to do until the exam.');

CALL delList(2);
-- should break
CALL delList(1000);

CALL getList(2);
-- should break
CALL getList(1000);

CALL getUserLists(2);
-- should break
CALL getUserLists(1000);

CALL putList(7, 'Awesomeness', 'work in progress!');
-- should break
CALL putList(1000, 'Awesomeness', 'work in progress!');

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
