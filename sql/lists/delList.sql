DELIMITER //
CREATE PROCEDURE delList
(
   IN user CHAR(255),
   IN list CHAR(255)
)
BEGIN
   DELETE FROM lists
      WHERE userId = userName2Id(user) AND
         list = listname;
END //
DELIMITER ;
