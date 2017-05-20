DELIMITER //
CREATE PROCEDURE addUser
(
   IN uName VARCHAR(255),
   IN uEmail VARCHAR(255),
   IN uPasswd BINARY(60),
   IN uAdmin BOOLEAN
)
BEGIN
   INSERT INTO users (userName, userEmail, userPassword, userAdmin)
      VALUES (uName, uEmail, uPasswd, uAdmin);

    IF(FOUND_ROWS() = 0) THEN
      SIGNAL SQLSTATE '52711'
        SET MESSAGE_TEXT = 'Unable to create the user.';
    END IF;
    SELECT userId FROM users WHERE userEmail = uEmail;
END //
DELIMITER ;
