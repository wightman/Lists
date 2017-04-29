DELIMITER //
CREATE PROCEDURE putUser
(
  IN uid INT,
  IN uName VARCHAR(255),
  IN uEmail VARCHAR(255)
)
BEGIN
   UPDATE users
      SET  userName = uName,
           userEmail = uEmail
      WHERE userId = uid;

   /* Error 52702: User not found*/
   IF(ROW_COUNT() = 0) THEN
     SIGNAL SQLSTATE '52702'
      SET MESSAGE_TEXT = 'User not found.';
   END IF;
END //
DELIMITER ;
