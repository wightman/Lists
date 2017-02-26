DELIMITER //
CREATE PROCEDURE putCollaborator
(
  IN uid INT,
  IN lid INT,
  IN rw CHAR(1)
)
BEGIN
   UPDATE collaborators
      SET  access = rw
      WHERE uId = userId AND lid = listId;
END //
DELIMITER ;
