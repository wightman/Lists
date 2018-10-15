DELIMITER //
CREATE PROCEDURE getCollaborator
(
  IN cId INT,
  IN lId INT
)
BEGIN
  SELECT userID as collaboratorID, accessType, collaboratorSince
    FROM collaborators
    WHERE listId = lId AND
      userId = cId;
END //
DELIMITER ;
