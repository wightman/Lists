DELIMITER //
CREATE PROCEDURE listCollaborators
(
   IN lid INT
)
BEGIN
   SELECT userID, access
      FROM collaborators
      WHERE listId = lid;
END //
DELIMITER ;
