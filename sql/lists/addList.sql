DELIMITER //
CREATE PROCEDURE addList
(
   IN user VARCHAR(255),
   IN list VARCHAR(255)
)
BEGIN
   INSERT INTO lists (listName, userId)
         VALUES (list, userName2Id(user));
END //
DELIMITER ;
