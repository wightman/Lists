DELIMITER //
CREATE PROCEDURE delTask
(
   IN user CHAR(255),
   IN list CHAR(255),
   IN task INT
)
BEGIN
   DELETE FROM tasks
      WHERE  listID = listName2Id(user, list) AND
         taskId = task;
END //
DELIMITER ;
