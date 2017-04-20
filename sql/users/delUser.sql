DELIMITER //
CREATE PROCEDURE delUser
(
   IN uId INT
)
BEGIN
   DELETE FROM users
      WHERE uId = userId;
   IF(ROW_COUNT() = 0) THEN
     SIGNAL SQLSTATE '77001'
     SET MESSAGE_TEXT = 'User does not exist';
   END IF;
END //
DELIMITER ;
