DELIMITER //
CREATE FUNCTION userName2Id(user VARCHAR(255))
    RETURNS INT
    NOT DETERMINISTIC

BEGIN
    DECLARE uid INT;
    SELECT userId INTO uid
       FROM users
       WHERE userName = user;

      RETURN(uid);
END //
DELIMITER ;
