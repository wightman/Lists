DELIMITER //
CREATE PROCEDURE getItem
(
  IN lId INT,
  IN iId INT
)
BEGIN
   SELECT *
     FROM items
     WHERE lId = listId AND iID = itemId;
   IF(FOUND_ROWS() = 0) THEN
     SIGNAL SQLSTATE '52730'
       SET MESSAGE_TEXT = 'Item not found.';
   END IF;
  END //
DELIMITER ;
