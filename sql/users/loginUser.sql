DELIMITER //
CREATE PROCEDURE loginUser
(
  IN uEmail VARCHAR(255),
  IN uPassword BINARY(60)
)
BEGIN
   SELECT userId, userName, userEmail, userAdmin, userSince
      FROM users
      WHERE userEmail = uEmail AND
            uPassword = userPassword;
      IF(ROW_COUNT() = 0) THEN
         CALL raise_application_error(77002, 'Bad credentials');
      END IF;
END //
DELIMITER ;
