DROP PROCEDURE putCollaboration;
DELIMITER //
CREATE PROCEDURE putCollaboration
(
  IN uId INT,
  IN lId INT
)
BEGIN
UPDATE collaborators
    SET collaborationViewed = TRUE
    WHERE listId = lId AND userId = uId;
  IF(FOUND_ROWS() = 0) THEN
    SIGNAL SQLSTATE '52720'
      SET MESSAGE_TEXT = 'Collaborator or list not found.';
  END IF;
END //
DELIMITER ;
