DELIMITER //
CREATE PROCEDURE putUser
(
  IN user VARCHAR(255),
  IN pass VARCHAR(255)
)
BEGIN
   UPDATE users
      SET  password = pass
      WHERE userId = userName2Id(user);
END //
DELIMITER ;
