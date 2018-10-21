DROP PROCEDURE getCollaborator;
DELIMITER //
CREATE PROCEDURE getCollaborator
(
  IN cId INT,
  IN lId INT
)
BEGIN
  SELECT userID as collaboratorId, listId, accessTYpe, collaboratorSince
    FROM collaborators
    WHERE listId = lId AND
      userId = cId;
END //
DELIMITER ;
