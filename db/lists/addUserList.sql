DELIMITER //
CREATE PROCEDURE addUserList
(
   IN uId INT,
   IN lname VARCHAR(255),
   IN lDescription VARCHAR(255)
)
BEGIN

  INSERT INTO lists (userId, listName, listDescription)
        VALUES (uId, lName, lDescription);

   /* Error 52701: Unable to add the user*/
   IF(ROW_COUNT() = 0) THEN
     SIGNAL SQLSTATE '52721'
       SET MESSAGE_TEXT = 'Unable to create the list.';
   END IF;

   SELECT LAST_INSERT_ID(); /* Specific to this session */
END //
DELIMITER ;
