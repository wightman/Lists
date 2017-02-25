DELIMITER //
CREATE PROCEDURE putUser
(
  IN uid INT,
  IN uName VARCHAR(255),
  IN uEmail VARCHAR(255),
  IN uAdmin BOOLEAN
)
BEGIN
   UPDATE users
      SET  userName = uName,
           userEmail = uEmail,
           userAdmin = uAdmin
      WHERE userId = uid;
END //
DELIMITER ;
