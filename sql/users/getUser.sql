DELIMITER //
CREATE PROCEDURE getUser
(
   IN id INT
)
BEGIN
   SELECT * FROM users
      WHERE id = userId;
END //
DELIMITER ;
