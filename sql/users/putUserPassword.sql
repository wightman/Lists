DELIMITER //
CREATE PROCEDURE putUserPassword
(
  IN uEmail VARCHAR(255),
  IN uPassword BINARY(60)
)
BEGIN
   SELECT  users
      SET  userPassword = uPassword
      WHERE userId = uid;
END //
DELIMITER ;
