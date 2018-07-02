-- build some users
CALL addUser('You', 'you@example.ca','$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a', true);
CALL addUser('Me', 'me@example.ca','$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a', true);
CALL addUser('Them', 'them@example.ca','$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a', false);
CALL addUser('Us', 'us@example.ca','$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a', false);

CALL delUser(4);
-- should break
CALL delUser(1000);

CALL getUser(1);
-- should break
CALL getUser(1000);

CALL getUserNames();
CALL getUsersAll();

CALL putUser(1, 'You', 'TheNewYou@example.ca');
-- should break
CALL putUser(1000, 'You', 'TheNewYou@example.ca');

CALL putUserAdmin(1, false);
CALL getUser(1);

CALL putUserAdmin(1, true);
CALL getUser(1);

-- should break
CALL putUserAdmin(1000, false);

CALL putUserPassword(1,'$FAIL0$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a');
-- should break
CALL putUserPassword(1000,'$FAIL0$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a');

CALL verifyUser('me@example.ca','$FAIL0$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a');
-- should break
CALL verifyUser('me@example.ca','$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a');
CALL verifyUser('us@example.ca','$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a');

-- All user table procedures work!

-- build a list
CALL addList(2, 'Stuff', NULL);
CALL addList(1,'INFO1103', 'To do before the end of term');
CALL addList(1, 'Stuff', NULL);

CALL delList(3);
-- should break
CALL delList(1000);

CALL getList(2);
-- should break
CALL getList(1000);

CALL getUserLists(1);
-- should break
CALL getUserLists(1000);

CALL putList(1, 'Awesomeness', 'work in progress!');
CALL putList(2,'INFO1103','Stuff I should have done.');
-- should break
CALL putList(1000, 'Awesomeness', 'work in progress!');

-- All user table procedures work!

-- build some tasks
CALL addItem(2, 'Haircut','Shorter, please',2, 1,false);
CALL addItem(2, 'School','Finish Assignment 3',1, 1,false);
CALL addItem(2, 'School','Finish Lab 5',1,2,false);

-- rid ourselves of one
CALL delItem(3);
-- should break
CALL deladdItem(1000);

-- what needs to be done?
CALL getListItems(2);
-- should break
CALL getListTasks(1000);

-- update list
CALL putItem(1, 'Hair tonic', 'please grow!',1,true);
CALL putItem(1000, 'Hair tonic', 'please grow!',1,false);

-- Make me a collaborator on your list
CALL addCollaborator(2,1,'R');
CALL addCollaborator(2,5,'W');
CALL addCollaborator(1,4,'R');
-- should break
CALL addCollaborator(2000,1,'R');
CALL addCollaborator(2,1000,'R');
CALL addCollaborator(2,1,'X');

-- remove a collaboration
CALL delCollaborator(2,1);
-- should break
CALL delCollaborator(1000,1);

-- list accessTypes
CALL getAccessTypes();

-- List collaborators and access for a listName
CALL getCollaborators(4);
CALL getCollaborators(1);

-- update a collaboration
CALL putCollaborator(2,5,'R');
-- should break
CALL putCollaborator(2,50,'R');
