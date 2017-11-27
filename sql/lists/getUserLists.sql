/* getUserLists: Return the list information for all lists that:
                 (i) a user owns
                 (ii) a user collaborates on
 */
 DELIMITER //
CREATE PROCEDURE getUserLists
(
  IN uId INT
)
BEGIN
   SELECT *
      FROM lists as l, collaborators as c
      WHERE userId = uId OR

   IF(FOUND_ROWS() = 0) THEN
      SIGNAL SQLSTATE '52720'
        SET MESSAGE_TEXT = 'User has no lists.';
    END IF;
END //
DELIMITER ;
