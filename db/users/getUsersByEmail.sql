DELIMITER //
CREATE PROCEDURE getUsersByEmail
(
  IN uEmailFragment VARCHAR(255)
)
BEGIN
   SELECT userId, userName, userEmail, userAdmin, userSince
      FROM users
      WHERE userEmail LIKE  CONCAT('%', uEmailFragment,'%');
END //
DELIMITER ;
