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

    IF(ROW_COUNT() = 0) THEN
      SIGNAL SQLSTATE '52711'
        SET MESSAGE_TEXT = 'Unable to create the user.';
    END IF;

    SELECT LAST_INSERT_ID(); /* Specific to this session */

END //
DELIMITER ;
