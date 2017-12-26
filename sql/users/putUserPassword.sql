DELIMITER //
DROP PROCEDURE IF EXISTS putUserPassword;
CREATE PROCEDURE putUserPassword
(
  IN uId INT,
  IN uPassword BINARY(60)
)
BEGIN
   UPDATE  users
      SET  userPassword = uPassword
      WHERE userId = uId;

    /* Error 52702: User not found*/
    IF(ROW_COUNT() = 0) THEN
      SIGNAL SQLSTATE '52710'
        SET MESSAGE_TEXT = 'User not found.';
    END IF;
END //
DELIMITER ;
