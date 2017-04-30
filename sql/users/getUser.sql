DELIMITER //
CREATE PROCEDURE getUser
(
   IN uId INT
)
BEGIN
   SELECT userId, userName, userEmail, userAdmin, userSince FROM users
      WHERE userId = uId;
  /* Error 52702: User not found*/
  IF(FOUND_ROWS() = 0) THEN
    SIGNAL SQLSTATE '52702'
      SET MESSAGE_TEXT = 'User not found.';
  END IF;
END //
DELIMITER ;
