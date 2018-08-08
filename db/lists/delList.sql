DELIMITER //
CREATE PROCEDURE delList
(
   IN uId INT,
   IN lId INT
)
BEGIN
   DELETE FROM lists
      WHERE
        listId = lId AND
        userID = uId;
        
    IF(ROW_COUNT() < 1) THEN
      SIGNAL SQLSTATE '52720'
        SET MESSAGE_TEXT = 'List owned by this user not found.';
    END IF;
END //
DELIMITER ;
