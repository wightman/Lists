DELIMITER //
CREATE PROCEDURE delTask
(
   IN tid INT
)
BEGIN
   DELETE FROM tasks
      WHERE taskId = tid;
END //
DELIMITER ;
