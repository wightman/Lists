DELIMITER //
CREATE PROCEDURE addCollaborator
(
   IN user INT,
   IN list INT,
   IN rw CHAR(1)
)
BEGIN
   INSERT INTO collaborators (userID, listID, access)
      VALUES (user, list, rw);
END //
DELIMITER ;
