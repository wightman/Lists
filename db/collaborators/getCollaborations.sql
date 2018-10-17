DELIMITER //
CREATE PROCEDURE getCollaborations
(
   IN uId INT
)
BEGIN
  SELECT userId as collaboratorId, listID, accessType
    FROM collaborators
    WHERE userId = cId;
  IF(FOUND_ROWS() = 0) THEN
    SIGNAL SQLSTATE '52720'
      SET MESSAGE_TEXT = 'List not found.';
  END IF;
END //
DELIMITER ;
