DROP PROCEDURE delCollaboration;
DELIMITER //
CREATE PROCEDURE delCollaboration
(
  IN uId INT,
  IN lId INT
)
BEGIN
  DELETE FROM collaborators
    WHERE userId = uId AND listId = lId;
  IF(ROW_COUNT() < 1) THEN
    SIGNAL SQLSTATE '52740'
      SET MESSAGE_TEXT = 'Collaboration not found.';
  END IF;
END //
DELIMITER ;
