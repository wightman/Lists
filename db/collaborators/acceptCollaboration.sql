DELIMITER //
CREATE PROCEDURE acceptCollaboration
(
  IN uId INT,
  IN lId INT
)
BEGIN
  UPDATE collaborators
    SET  collaborationViewed = TRUE
    WHERE userId = uId AND listId = lId;
  IF(ROW_COUNT() = 0) THEN
    SIGNAL SQLSTATE '52740'
      SET MESSAGE_TEXT = 'Collaboration not found.';
  END IF;
END //
DELIMITER ;
