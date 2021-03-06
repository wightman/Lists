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
     WHERE
       listId = lId AND
       userID = uId;
  IF(ROW_COUNT() = 0) THEN
    SIGNAL SQLSTATE '52720'
      SET MESSAGE_TEXT = 'List not found.';
  END IF;
END //
DELIMITER ;
