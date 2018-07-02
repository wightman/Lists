DELIMITER //
CREATE PROCEDURE getItem
(
  IN lId INT
  IN iId INT
)
BEGIN
   SELECT *
     FROM items
     WHERE lId = listId AND iID = itemId
     ORDER BY itemPosition;
   IF(FOUND_ROWS() = 0) THEN
     SIGNAL SQLSTATE '52730'
       SET MESSAGE_TEXT = 'List not found.';
   END IF;
  END //
DELIMITER ;
