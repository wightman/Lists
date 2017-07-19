DELIMITER //
CREATE PROCEDURE putUserAdmin
(
  IN uId INT,
  IN uAdmin BOOLEAN
)
BEGIN
   UPDATE users
      SET  userAdmin = uAdmin
      WHERE userId = uId;

    /* Error 52702: User not found*/
    IF(ROW_COUNT() = 0) THEN
      SIGNAL SQLSTATE '52710'
        SET MESSAGE_TEXT = 'User not found.';
    END IF;
END //
DELIMITER ;
