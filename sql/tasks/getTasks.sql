DELIMITER //
CREATE PROCEDURE getTasks
(
   IN user CHAR(255),
   IN list CHAR(255),
)
BEGIN
   SELECT * FROM tasks
      WHERE  listID = listName2Id(user, list);
END //
DELIMITER ;
