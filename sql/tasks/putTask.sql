DELIMITER //
CREATE PROCEDURE putTask
(
  IN tId INT,
  IN item VARCHAR(255),
  IN done BOOLEAN
)
BEGIN
   UPDATE tasks
      SET  completed = done, task = item
      WHERE tid = taskId;
END //
DELIMITER ;
