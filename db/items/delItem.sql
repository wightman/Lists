DELIMITER //
CREATE PROCEDURE delItem
(
   IN lId INT,
   IN iId INT
)
BEGIN
   DELETE FROM items
      WHERE listId = lId AND itemId = iId;
    IF(ROW_COUNT() < 1) THEN
      SIGNAL SQLSTATE '52730'
        SET MESSAGE_TEXT = 'Item not found.';
    END IF;
END //
DELIMITER ;
