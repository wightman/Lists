DELIMITER //
CREATE PROCEDURE putUserAdmin
(
  IN uid INT,
  IN uAdmin BOOLEAN
)
BEGIN
   UPDATE users
      SET  userAdmin = uAdmin
      WHERE userId = uid;

    /* Error 52702: User not found*/
    IF(ROW_COUNT() = 0) THEN
      SIGNAL SQLSTATE '52702'
        SET MESSAGE_TEXT = 'User not found.';
    END IF;
END //
DELIMITER ;
