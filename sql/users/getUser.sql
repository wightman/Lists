DELIMITER //
CREATE PROCEDURE getUser
(
   IN user VARCHAR(255)
)
BEGIN
   SELECT * FROM users
      WHERE user = userName;
END //
DELIMITER ;
