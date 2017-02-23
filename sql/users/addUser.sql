DELIMITER //
CREATE PROCEDURE addUser
(
   IN name CHAR(255),
   IN mail VARCHAR(255),
   IN password BINARY(60),
   IN admin BOOLEAN
)
BEGIN
   INSERT INTO users (userName, userEmail, userPassword, userAdmin)
      VALUES (name, email, passwd, admin);
END //
DELIMITER ;
