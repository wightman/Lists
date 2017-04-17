DELIMITER //
CREATE PROCEDURE putTask
(
  IN tId INT,
  IN task VARCHAR(255),
  IN taskDetail VARCHAR(255),
  IN pos INT,
  IN done BOOLEAN
)
BEGIN
   UPDATE tasks
      SET  completed = done,
           taskName = task,
           taskDescription = taksDetail, 
           taskPosition = pos
      WHERE tid = taskId;
END //
DELIMITER ;
