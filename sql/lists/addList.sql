DELIMITER //
CREATE PROCEDURE addList
(
   IN uId INT,
   IN lname VARCHAR(255),
   IN lDescription VARCHAR(255)
)
BEGIN
  IF(lDescription = NULL)THEN
    INSERT INTO lists (userId, listName)
        VALUES (uId, lName);
  ELSE
    INSERT INTO lists (userId, listName, listDescription)
        VALUES (uId, lName, lDescription);
  END IF;
   /* Error 52701: Unable to add the user*/
   IF(FOUND_ROWS() = 0) THEN
     SIGNAL SQLSTATE '52703'
       SET MESSAGE_TEXT = 'Unable to create the list.';
   END IF;
END //
DELIMITER ;
