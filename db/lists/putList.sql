DELIMITER //
CREATE PROCEDURE putList
(
  IN lId INT,
  IN lName VARCHAR(255),
  IN lDescription VARCHAR(255)
)
BEGIN
   UPDATE lists
      SET listName = lName,
          listDescription = lDescription
      WHERE listId = lId;
  IF(ROW_COUNT() = 0) THEN
    SIGNAL SQLSTATE '52720'
      SET MESSAGE_TEXT = 'List not found.';
  END IF;
END //
DELIMITER ;
