DELIMITER //
CREATE PROCEDURE putTask
(
  IN tId INT,
  IN tName VARCHAR(255),
  IN tDetail VARCHAR(255),
  IN tPos INT,
  IN done BOOLEAN
)
BEGIN
   UPDATE tasks
      SET  completed = done,
           taskName = tName,
           taskDetail = tDetail,
           taskPosition = tPos
      WHERE tId = taskId;
    IF(ROW_COUNT() = 0) THEN
      SIGNAL SQLSTATE '52706'
        SET MESSAGE_TEXT = 'Task not found.';
    END IF;
END //
DELIMITER ;
