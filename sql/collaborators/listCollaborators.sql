DELIMITER //
CREATE PROCEDURE listCollaborators
(
   IN lid INT
)
BEGIN
   SELECT userID as collaboratorID, access
      FROM collaborators
      WHERE listId = lid;
END //
DELIMITER ;
