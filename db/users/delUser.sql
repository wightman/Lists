DELIMITER //
CREATE PROCEDURE delUser
(
   IN uId INT
)
BEGIN
   DELETE FROM users
      WHERE userId = uId;
  /* Error 52702: User not found*/
  IF(ROW_COUNT() < 1) THEN
    SIGNAL SQLSTATE '52710'
      SET MESSAGE_TEXT = 'User not found.';
  END IF;
END //
DELIMITER ;
