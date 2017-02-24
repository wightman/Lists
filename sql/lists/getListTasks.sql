DELIMITER //
CREATE PROCEDURE getListTasks
(
  IN lid INT
)
BEGIN
   SELECT *
   FROM tasks
   WHERE lid = listId;
END //
DELIMITER ;
