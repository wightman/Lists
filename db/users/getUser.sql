DELIMITER //
CREATE PROCEDURE getUser
(
   IN uId INT
)
BEGIN
   SELECT userId, userName, userEmail, userAdmin, userSince FROM users
      WHERE userId = uId;
  IF(FOUND_ROWS() = 0) THEN
    SIGNAL SQLSTATE '52710'
      SET MESSAGE_TEXT = 'User not found.';
  END IF;
END //
DELIMITER ;
