DELIMITER //
CREATE PROCEDURE addTask
(
   IN lid INT,
   IN task VARCHAR(255),
   IN taskPos INT,
   IN done BOOLEAN
)
BEGIN
   INSERT INTO tasks (listId, task, taskPosition, completed)
         VALUES (lid, task, taskPos, done);
END //
DELIMITER ;
