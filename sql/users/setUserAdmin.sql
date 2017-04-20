DELIMITER //
CREATE PROCEDURE setUserAdmin
(
  IN uid INT,
  IN uAdmin BOOLEAN
)
BEGIN
   UPDATE users
      SET  userAdmin = uAdmin
      WHERE userId = uid;
   IF(ROW_COUNT() = 0) THEN
     SIGNAL SQLSTATE '77001'
     SET MESSAGE_TEXT = 'User does not exist';
   END IF;
END //
DELIMITER ;
