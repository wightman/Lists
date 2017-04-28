DELIMITER //
CREATE PROCEDURE throwError
(
)
BEGIN
   DECLARE rowCount INT DEFAULT 0;
   SELECT *
      FROM users
      WHERE userId = 666;

   SELECT ROW_COUNT() into rowCount;
   IF rowCount < 1 THEN
     SIGNAL SQLSTATE '42000'
     SET MESSAGE_TEXT = 'Throw all the errors!';
   END IF;
END //
DELIMITER ;
