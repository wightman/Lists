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

      /* Error 52721: Unable to create the list*/
      IF(ROW_COUNT() = 0) THEN
        SIGNAL SQLSTATE '52721'
          SET MESSAGE_TEXT = 'Unable to create the list.';
      END IF;
    SET @LastInsertId = LAST_INSERT_ID(); /* Specific to this session */
    /* Need to store this to return it after the next stage of
      adding a record to the Collaborator table */
    CALL addCollaborator(uId,@LastInsertId,'O');
    /* Error 52721: Unable to create the list*/
    IF(ROW_COUNT() = 0) THEN
      CALL delList(uId,@LastInsertId);
      SIGNAL SQLSTATE '52721'
        SET MESSAGE_TEXT = 'Unable to create the list.';
    END IF;
    SELECT @LastInsertId;
END //
DELIMITER ;
