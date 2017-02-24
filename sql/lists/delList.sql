DELIMITER //
CREATE PROCEDURE delList
(
   IN user CHAR(255),
   IN list CHAR(255)
)
BEGIN
   DELETE FROM lists
      WHERE user = userId AND
         list = listName;
END //
DELIMITER ;
