DELIMITER //
DROP PROCEDURE IF EXISTS getUsersByEmail;
CREATE PROCEDURE getUsersByEmail
(
  IN uEmail VARCHAR(255)
)
BEGIN
   SELECT userId, userName, userEmail, userAdmin, userSince
    FROM users
    WHERE LOWER(userEmail) LIKE LOWER(CONCAT('%',uEmail,'%'));
END //
DELIMITER ;
