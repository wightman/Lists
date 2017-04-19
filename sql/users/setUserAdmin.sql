DELIMITER //
CREATE PROCEDURE setUserAdmin
(
  IN uid INT,
  IN uAdmin BOOLEAN
)
BEGIN
   UPDATE users
      SET  userAdmin = uAdmin
      WHERE userId = uid;
   IF(ROW_COUNT() = 0) THEN
     CALL raise_application_error(77001, 'User does not exist');
   END IF;
END //
DELIMITER ;
