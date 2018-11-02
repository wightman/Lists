DROP PROCEDURE addCollaborators;
DELIMITER //
CREATE PROCEDURE addCollaborator
(
   IN uId INT,
   IN lId INT,
   IN orw CHAR(1)
)
BEGIN
  INSERT INTO collaborators (userId, listId, accessType)
    VALUES (uId, lId, orw);
  IF(ROW_COUNT() = 0) THEN
    SIGNAL SQLSTATE '52707'
      SET MESSAGE_TEXT = 'Unable to create the collaboration.';
  END IF;

  SELECT LAST_INSERT_ID(); /* Specific to this session */

END //
DELIMITER ;
