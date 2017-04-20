DELIMITER //
CREATE PROCEDURE putUserPassword
(
  IN uid INT,
  IN uPassword BINARY(60)
)
BEGIN
   UPDATE  users
      SET  userPassword = uPassword
      WHERE userId = uid;
  IF(ROW_COUNT() = 0) THEN
    SIGNAL SQLSTATE '77001'
    SET MESSAGE_TEXT = 'User does not exist';
  END IF;
END //
DELIMITER ;
