DELIMITER //
CREATE PROCEDURE addList
(
   IN id INT,
   IN lname VARCHAR(255)
)
BEGIN
   INSERT INTO lists (listName, userId)
         VALUES (lname, id);
END //
DELIMITER ;
