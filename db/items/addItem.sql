DROP PROCEDURE addItem;
DELIMITER //
CREATE PROCEDURE addItem
(
   IN lid INT,
   IN iName VARCHAR(255),
   IN iDetail VARCHAR(255),
   IN cId INT
)
BEGIN
   INSERT INTO items (listId, itemName, itemDetail, creatorId)
         VALUES (lid, iName, iDetail, cId);
  IF(ROW_COUNT() = 0) THEN
     SIGNAL SQLSTATE '52731'
       SET MESSAGE_TEXT = 'Unable to create the item.';
   END IF;

   SELECT LAST_INSERT_ID(); /* Specific to this session */

END //
DELIMITER ;
