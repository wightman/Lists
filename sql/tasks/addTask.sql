DELIMITER //
CREATE PROCEDURE addTask
(
   IN lid INT,
   IN task VARCHAR(255),
   IN taskDetail VARCHAR(255),
   IN taskPos INT,
   IN done BOOLEAN
)
BEGIN
   INSERT INTO tasks (listId, taskName, taskDescription, taskPosition, completed)
         VALUES (lid, task, taskDetail, taskPos, done);
END //
DELIMITER ;
