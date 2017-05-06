DELIMITER //
CREATE PROCEDURE delList
(
   IN lId INT
)
BEGIN
   DELETE FROM lists
      WHERE listId = lId;
    IF(ROW_COUNT() < 1) THEN
      SIGNAL SQLSTATE '52720'
        SET MESSAGE_TEXT = 'List not found.';
    END IF;
END //
DELIMITER ;
