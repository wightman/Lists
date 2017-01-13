DELIMITER //
CREATE PROCEDURE delUser
(
   IN user VARCHAR(255)
)
BEGIN
   DELETE FROM users
      WHERE user = userName;
END //
DELIMITER ;
