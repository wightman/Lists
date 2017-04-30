DELIMITER //
CREATE PROCEDURE verifyUser
(
  IN uEmail VARCHAR(255),
  IN uPassword BINARY(60)
)
BEGIN
   SELECT userId, userName, userEmail, userAdmin, userSince
      FROM users
      WHERE userEmail = uEmail AND
            userPassword = uPassword;

    /* Error 52702: User not found*/
    IF(FOUND_ROWS() = 0) THEN
      SIGNAL SQLSTATE '52700'
        SET MESSAGE_TEXT = 'Bad credentials.';
    END IF;
END //
DELIMITER ;
