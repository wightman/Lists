DELIMITER //
CREATE PROCEDURE getUserLists
(
  IN uid INT
)
BEGIN
   SELECT listname, listId
      FROM lists
      WHERE userid = uid;
END //
DELIMITER ;
