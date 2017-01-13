DELIMITER //
CREATE FUNCTION listName2Id(user VARCHAR(255),list VARCHAR(255))
    RETURNS INT
    NOT DETERMINISTIC

BEGIN
    DECLARE lid INT;
    SELECT listId INTO lid
       FROM lists
       WHERE listName = list AND userId = userName2Id(user);

      RETURN(lid);
END //
DELIMITER ;
