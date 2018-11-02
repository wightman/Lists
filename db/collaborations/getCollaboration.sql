DROP PROCEDURE getCollaboration;
DELIMITER //
CREATE PROCEDURE getCollaboration
(
  IN uId INT,
  IN lId INT
)
BEGIN
SELECT C.userId, L.userId as ownerId, C.listId, accessType, collaboratorSince
    FROM collaborators as C, lists as L
    WHERE L.listId = C.listId AND C.userId = uId AND C.listId = lId;
  IF(FOUND_ROWS() = 0) THEN
    SIGNAL SQLSTATE '52720'
      SET MESSAGE_TEXT = 'Collaborator not found.';
  END IF;
END //
DELIMITER ;
