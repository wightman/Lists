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
      CALL raise_application_error(77001, 'User does not exist');
   END IF;
END //
DELIMITER ;
