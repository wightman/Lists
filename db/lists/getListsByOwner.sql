DELIMITER //
CREATE PROCEDURE getListsByOwner
(
  IN uId INT
)
BEGIN
   SELECT userId AS 'OwnerId',
      listId, listName, listDescription, listSince
      FROM lists
      WHERE userId = uId;
END //
DELIMITER ;
