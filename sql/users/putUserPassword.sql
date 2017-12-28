DELIMITER //
DROP PROCEDURE IF EXISTS putUserPassword;
CREATE PROCEDURE putUserPassword
(
  IN uId INT,
  IN uPassword BINARY(60),
  IN uNewPassword BINARY(60)
)
BEGIN
   UPDATE  users
      SET  userPassword = uNewPassword
      WHERE userId = uId AND userPassword = uPassword;

    /* Error 52702: User not found*/
    IF(ROW_COUNT() = 0) THEN
      SIGNAL SQLSTATE '52710'
        SET MESSAGE_TEXT = 'Unable to update password.';
    END IF;
END //
DELIMITER ;
