DELIMITER //
CREATE PROCEDURE addList
(
   IN uId INT,
   IN lname VARCHAR(255),
   IN lDescription VARCHAR(255)
)
BEGIN
  DECLARE LastInsertId MEDIUMINT;
  DECLARE EXIT HANDLER FOR SQLEXCEPTION, SQLWARNING
  BEGIN
    ROLLBACK;
    SIGNAL SQLSTATE '52721'
      SET MESSAGE_TEXT = 'Unable to create the list.';
  END;

  START TRANSACTION;
    INSERT INTO lists (listName, listDescription, userId)
      VALUES (lName, lDescription, uId);
    SET LastInsertId = LAST_INSERT_ID();
    CALL addCollaborator(uId,LastInsertId,'O');
  COMMIT;
  SELECT LastInsertId;
END //
DELIMITER ;
