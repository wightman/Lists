DELIMITER //
CREATE PROCEDURE getUserLists
(
  IN uId INT
)
BEGIN
   SELECT listId
      FROM lists
      WHERE userId = uId;
    IF(FOUND_ROWS() = 0) THEN
      SIGNAL SQLSTATE '52720'
        SET MESSAGE_TEXT = 'User not found.';
    END IF;
END //
DELIMITER ;
