DELIMITER //
CREATE PROCEDURE addUser
(
   IN name VARCHAR(255),
   IN email VARCHAR(255),
   IN passwd BINARY(60),
   IN admin BOOLEAN
)
BEGIN
   INSERT INTO users (userName, userEmail, userPassword, userAdmin)
      VALUES (name, email, passwd, admin);
END //
DELIMITER ;
