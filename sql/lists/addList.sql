DELIMITER //
CREATE PROCEDURE addList
(
   IN uId INT,
   IN lname VARCHAR(255),
   IN lDescription VARCHAR(255)
)
BEGIN

  INSERT INTO lists (userId, listName, listDescription)
        VALUES (uId, lName, lDescription);

   /* Error 52701: Unable to add the user*/
   IF(FOUND_ROWS() = 0) THEN
     SIGNAL SQLSTATE '52703'
       SET MESSAGE_TEXT = 'Unable to create the list.';
   END IF;
END //
DELIMITER ;
