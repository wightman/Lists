DELIMITER //
CREATE PROCEDURE getList
(
  IN uId INT,
  IN lId INT
)
BEGIN
   SELECT L.listId, L.listName, L.listDescription, L.userId, L.listSince,
   C.access, C.collaboratorSince
   FROM lists as L JOIN collaborators AS C
   ON L.listId = C.listId
   WHERE
     L.listId = lId AND
     L.userID = uId AND
     access = 'O';

  IF(FOUND_ROWS() = 0) THEN
    SIGNAL SQLSTATE '52720'
      SET MESSAGE_TEXT = 'List not found.';
  END IF;
END //
DELIMITER ;
