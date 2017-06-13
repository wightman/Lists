DELIMITER //
CREATE PROCEDURE addTask
(
   IN lid INT,
   IN tName VARCHAR(255),
   IN tDetail VARCHAR(255),
   IN tPos INT,
   IN cId INT,
   IN done BOOLEAN
)
BEGIN
   INSERT INTO tasks (listId, taskName, taskDetail, taskPosition, creatorId,completed)
         VALUES (lid, tName, tDetail, tPos, cId, done);
  IF(ROW_COUNT() = 0) THEN
     SIGNAL SQLSTATE '52731'
       SET MESSAGE_TEXT = 'Unable to create the task.';
   END IF;

   SELECT LAST_INSERT_ID(); /* Specific to this session */

END //
DELIMITER ;
