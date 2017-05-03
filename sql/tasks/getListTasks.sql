DELIMITER //
CREATE PROCEDURE getListTasks
(
  IN lid INT
)
BEGIN
   SELECT *
     FROM tasks
     WHERE lid = listId
     ORDER BY taskPosition;
   IF(FOUND_ROWS() = 0) THEN
     SIGNAL SQLSTATE '52704'
       SET MESSAGE_TEXT = 'List not found.';
   END IF;
  END //
DELIMITER ;
