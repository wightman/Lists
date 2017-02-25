DELIMITER //
CREATE PROCEDURE getUser
(
   IN id INT
)
BEGIN
   SELECT userId, userName, userEmail, userAdmin, userSince FROM users
      WHERE id = userId;
END //
DELIMITER ;
