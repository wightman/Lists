DELIMITER //
CREATE PROCEDURE putUserPassword
(
  IN user VARCHAR(255),
  IN pass VARCHAR(255)
)
BEGIN
   UPDATE users
      SET  userPassword = pass
      WHERE userId = userName2Id(user);
END //
DELIMITER ;
