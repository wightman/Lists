DELIMITER //
CREATE PROCEDURE putItem
(
  IN iId INT,
  IN iName VARCHAR(255),
  IN iDetail VARCHAR(255),
  IN iPos INT,
  IN done BOOLEAN
)
BEGIN
   UPDATE items
      SET  completed = done,
           itemName = iName,
           itemDetail = iDetail,
           itemPosition = iPos
      WHERE iId = itemId;
    IF(ROW_COUNT() = 0) THEN
      SIGNAL SQLSTATE '52730'
        SET MESSAGE_TEXT = 'Task not found.';
    END IF;
END //
DELIMITER ;
