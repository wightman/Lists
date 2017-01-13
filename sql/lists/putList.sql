DELIMITER //
CREATE PROCEDURE putList
(
  IN lId INT,
  IN list VARCHAR(255)
)
BEGIN
   UPDATE lists
      SET listName = list
      WHERE lid = listId;
END //
DELIMITER ;
