DROP PROCEDURE getAccessTypes;
DELIMITER //
CREATE PROCEDURE getAccessTypes
(
)
BEGIN
   SELECT *
      FROM accessTypes;
END //
DELIMITER ;
