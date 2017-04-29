DELIMITER //
CREATE PROCEDURE getUser
(
   IN id INT
)
BEGIN
   SELECT userId, userName, userEmail, userAdmin, userSince FROM users
      WHERE id = userId;
  /* Error 52702: User not found*/
  IF( FOUND_ROWS() = 0) THEN
    SIGNAL SQLSTATE '52702'
      SET MESSAGE_TEXT = 'User not found.';
  END IF;
END //
DELIMITER ;
