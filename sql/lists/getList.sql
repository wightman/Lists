DELIMITER //
CREATE PROCEDURE getList
(
  IN lid INT
)
BEGIN
   SELECT *
      FROM lists
      WHERE listId = lId;
    IF(FOUND_ROWS() = 0) THEN
      SIGNAL SQLSTATE '52720'
        SET MESSAGE_TEXT = 'List not found.';
    END IF;
END //
DELIMITER ;
