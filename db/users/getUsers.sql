DELIMITER //
CREATE PROCEDURE getUsers()
BEGIN
   SELECT userId, userName, userEmail, userAdmin, userSince FROM users;
END //
DELIMITER ;
