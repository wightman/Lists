DELIMITER //
CREATE PROCEDURE getList
(
  IN lid INT
)
BEGIN
   SELECT *
      FROM lists
      WHERE lid = listId;
END //
DELIMITER ;
