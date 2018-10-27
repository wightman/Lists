DROP PROCEDURE getCollaborators;
DELIMITER //
CREATE PROCEDURE getCollaborators
(
   IN lId INT
)
BEGIN
SELECT userID as collaboratorId, listId, accessType, collaboratorSince
    FROM collaborators
    WHERE listId = lId;
  IF(FOUND_ROWS() = 0) THEN
    SIGNAL SQLSTATE '52720'
      SET MESSAGE_TEXT = 'List not found.';
  END IF;
END //
DELIMITER ;
