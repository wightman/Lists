DELIMITER //
CREATE PROCEDURE getUsersByName
(
  IN uNameFragment VARCHAR(255)
)
BEGIN
   SELECT userId, userName, userEmail, userAdmin, userSince
      FROM users
      WHERE userName LIKE  CONCAT('%', uNameFragment,'%');
END //
DELIMITER ;
