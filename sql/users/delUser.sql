DELIMITER //
CREATE PROCEDURE delUser
(
   IN id INT
)
BEGIN
   DELETE FROM users
      WHERE id = userId;
END //
DELIMITER ;
