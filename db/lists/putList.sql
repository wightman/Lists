DELIMITER //
CREATE PROCEDURE putList
(
  IN uId INT,
  IN lId INT,
  IN lName VARCHAR(255),
  IN lDescription VARCHAR(255)
)
/*  Collaborations identifies list accesstype for each collaborator/user
 */
BEGIN
  UPDATE lists
     SET listName = lName,
         listDescription = lDescription
     FROM lists as L, collaborators AS C
     WHERE
       C.listId = L.listId AND
       listId = lId AND
       userID = uId AND
       access <> 'R';
  IF(ROW_COUNT() = 0) THEN
    SIGNAL SQLSTATE '52720'
      SET MESSAGE_TEXT = 'Bad list ID or access type.';
  END IF;
END //
DELIMITER ;
