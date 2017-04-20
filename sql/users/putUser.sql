DELIMITER //
CREATE PROCEDURE putUser
(
  IN uid INT,
  IN uName VARCHAR(255),
  IN uEmail VARCHAR(255),
  IN uAdmin BOOLEAN
)
BEGIN
   UPDATE users
      SET  userName = uName,
           userEmail = uEmail,
           userAdmin = uAdmin
      WHERE userId = uid;
   IF(ROW_COUNT() = 0) THEN
     SIGNAL SQLSTATE '77001'
     SET MESSAGE_TEXT = 'User does not exist';
   END IF;
END //
DELIMITER ;
