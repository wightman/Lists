DROP PROCEDURE getItems;
DELIMITER //
CREATE PROCEDURE getItems
(
  IN lId INT
)
BEGIN
SELECT *
    FROM items
    WHERE listId = lId;
END //
DELIMITER ;
