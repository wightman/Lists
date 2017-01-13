DELIMITER //
CREATE PROCEDURE getList
(
  IN user VARCHAR(255),
  IN list VARCHAR(255)
)
BEGIN
   SELECT listname, listId
      FROM lists
      WHERE userid = userName2Id(user) AND
      list = listName;
END //
DELIMITER ;
