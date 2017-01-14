DELIMITER //
CREATE PROCEDURE addUser
(
   IN name CHAR(255),
   IN passwd CHAR(255),
   IN administrate BOOLEAN
)
BEGIN
   INSERT INTO users (userName, userPassword, userAdmin)
      VALUES (name, passwd, administrate);
END //
DELIMITER ;
