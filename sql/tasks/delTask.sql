DELIMITER //
CREATE PROCEDURE delTask
(
   IN tid INT
)
BEGIN
   DELETE FROM tasks
      WHERE taskId = tid;
    IF(ROW_COUNT() < 1) THEN
      SIGNAL SQLSTATE '52706'
        SET MESSAGE_TEXT = 'Task not found.';
    END IF;
END //
DELIMITER ;
