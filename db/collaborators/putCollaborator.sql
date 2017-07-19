DELIMITER //
CREATE PROCEDURE putCollaborator
(
  IN uId INT,
  IN lId INT,
  IN rw CHAR(1)
)
BEGIN
  UPDATE collaborators
    SET  access = rw
    WHERE userId = uId AND listId = lId;
  IF(ROW_COUNT() = 0) THEN
    SIGNAL SQLSTATE '52740'
      SET MESSAGE_TEXT = 'Collaboration not found.';
  END IF;
END //
DELIMITER ;
