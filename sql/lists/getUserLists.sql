DELIMITER //
CREATE PROCEDURE getUserLists
(
  IN uId INT
)
BEGIN
   SELECT *
      FROM lists
      WHERE userId = uId;
    IF(FOUND_ROWS() = 0) THEN
      SIGNAL SQLSTATE '52702'
        SET MESSAGE_TEXT = 'User not found.';
    END IF;
END //
DELIMITER ;
