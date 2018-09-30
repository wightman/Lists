DELIMITER //
CREATE PROCEDURE getUsersByAdmin
(
  IN uAdmin INT
)
BEGIN
   SELECT userId, userName, userEmail, userAdmin, userSince
      FROM users
      WHERE userAdmin = uAdmin;
END //
DELIMITER ;
