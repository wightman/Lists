DELIMITER //
CREATE PROCEDURE putUserPassword
(
  IN uid INT,
  IN uPassword BINARY(60)
)
BEGIN
   SELECT  users
      SET  userPassword = uPassword
      WHERE userId = uid;
END //
DELIMITER ;
