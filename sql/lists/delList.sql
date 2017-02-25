DELIMITER //
CREATE PROCEDURE delList
(
   IN lid INT
)
BEGIN
   DELETE FROM lists
      WHERE listId = lid;
END //
DELIMITER ;
