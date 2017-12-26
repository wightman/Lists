DELIMITER //
DROP PROCEDURE IF EXISTS getUsersByAdmin;
CREATE PROCEDURE getUsersByAdmin
(
  IN uAdmin BOOLEAN
)
BEGIN
   SELECT userId, userName, userEmail, userAdmin, userSince
    FROM users
    WHERE userAdmin = uAdmin;
END //
DELIMITER ;
