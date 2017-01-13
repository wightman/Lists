DELIMITER //
CREATE PROCEDURE addTask
(
   IN user VARCHAR(255),
   IN list VARCHAR(255),
   IN task VARCHAR(255),
   IN done BOOLEAN
)
BEGIN
   INSERT INTO tasks (listId, task, completed)
         VALUES (listName2Id(user,list), task, done);
END //
DELIMITER ;
