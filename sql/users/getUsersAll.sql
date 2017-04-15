DELIMITER //
CREATE PROCEDURE getUsersAll
(
)
BEGIN
   SELECT userId, userName, userEmail, userAdmin, userSince FROM users//
END //
DELIMITER ;
