DELIMITER //
CREATE PROCEDURE delCollaborator
(
  IN uid INT,
  IN lid INT
)
BEGIN
   DELETE FROM collaborators
    WHERE uid = userId AND lid = listId;
END //
DELIMITER ;
