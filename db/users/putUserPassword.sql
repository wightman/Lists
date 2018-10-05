DELIMITER //
CREATE PROCEDURE putUserPassword
(
  IN uId INT,
  IN uPassword BINARY(60),
  IN nPassword BINARY(60)
)
BEGIN
   UPDATE  users
      SET  userPassword = nPassword
      WHERE userId = uId AND userPassword = uPassword;

    /* Error 52702: User not found*/
    IF(ROW_COUNT() = 0) THEN
      SIGNAL SQLSTATE '52710'
        SET MESSAGE_TEXT = 'Bad credentials.';
    END IF;
END //
DELIMITER ;
