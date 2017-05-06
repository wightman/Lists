DELIMITER //
CREATE PROCEDURE getCollaborators
(
   IN lId INT
)
BEGIN
  SELECT userID as collaboratorID, access
    FROM collaborators
    WHERE listId = lId;
  IF(FOUND_ROWS() = 0) THEN
    SIGNAL SQLSTATE '52720'
      SET MESSAGE_TEXT = 'List not found.';
  END IF;
END //
DELIMITER ;
