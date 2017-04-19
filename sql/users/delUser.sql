DELIMITER //
CREATE PROCEDURE delUser
(
   IN uId INT
)
BEGIN
   DELETE FROM users
      WHERE uId = userId;
   IF(ROW_COUNT() = 0) THEN
      CALL raise_application_error(77001, 'User does not exist');
   END IF;
END //
DELIMITER ;
