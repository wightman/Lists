DELIMITER //
CREATE PROCEDURE putTask
(
  IN tId INT,
  IN item VARCHAR(255),
  IN pos INT,
  IN done BOOLEAN
)
BEGIN
   UPDATE tasks
      SET  completed = done,
           task = item, 
           taskPosition = pos
      WHERE tid = taskId;
END //
DELIMITER ;
