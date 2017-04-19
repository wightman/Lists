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
     CALL raise_application_error(77001, 'User does not exist');
  END IF;
END //
DELIMITER ;
