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
END //
DELIMITER ;
