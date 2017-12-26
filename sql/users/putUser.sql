DELIMITER //
DROP PROCEDURE IF EXISTS putUser;
CREATE PROCEDURE putUser
(
  IN uId INT,
  IN uName VARCHAR(255),
  IN uEmail VARCHAR(255))
BEGIN
   UPDATE users
      SET  userName = uName,
        userEmail = uEmail
      WHERE userId = uId;

   /* Error 52702: User not found*/
   IF(ROW_COUNT() = 0) THEN
     SIGNAL SQLSTATE '52710'
      SET MESSAGE_TEXT = 'User not found.';
   END IF;
END //
DELIMITER ;
