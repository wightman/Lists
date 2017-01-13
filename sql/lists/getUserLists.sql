DELIMITER //
CREATE PROCEDURE getUserLists
(
  IN user VARCHAR(255)
)
BEGIN
   SELECT listname, listId
      FROM lists
      WHERE userid = userName2Id(user);
END //
DELIMITER ;
