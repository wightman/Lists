DELIMITER //
CREATE PROCEDURE delUser
(
   IN uId INT
)
BEGIN
   DELETE FROM users
      WHERE uId = userId;
  /* Error 52702: User not found*/
  IF(ROW_COUNT() < 1) THEN
    SIGNAL SQLSTATE '52702'
      SET MESSAGE_TEXT = 'User not found.';
  END IF;
END //
DELIMITER ;
