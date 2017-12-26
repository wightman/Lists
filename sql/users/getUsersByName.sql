DELIMITER //
DROP PROCEDURE IF EXISTS getUsersByName;
CREATE PROCEDURE getUsersByName
(
  IN uName VARCHAR(255)
)
BEGIN
   SELECT userId, userName, userEmail, userAdmin, userSince
    FROM users
    WHERE LOWER(userName) LIKE LOWER(CONCAT('%',uName,'%'));
END //
DELIMITER ;
