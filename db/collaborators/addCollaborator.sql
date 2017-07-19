DELIMITER //
CREATE PROCEDURE addCollaborator
(
   IN uId INT,
   IN lId INT,
   IN rw CHAR(1)
)
BEGIN
  -- user shouldn't be the list owner
  SELECT userId
    FROM lists
    WHERE listId = lId AND userId = uId;
  IF(FOUND_ROWS() > 0) THEN
    SIGNAL SQLSTATE '52742'
      SET MESSAGE_TEXT = 'List owner cannot be a collaborator.';
  END IF;
  INSERT INTO collaborators (userId, listId, access)
    VALUES (uId, lId, rw);
  IF(ROW_COUNT() = 0) THEN
    SIGNAL SQLSTATE '52707'
      SET MESSAGE_TEXT = 'Unable to create the collaboration.';
  END IF;

  SELECT LAST_INSERT_ID(); /* Specific to this session */

END //
DELIMITER ;
