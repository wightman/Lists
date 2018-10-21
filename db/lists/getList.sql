DROP PROCEDURE getList;
DELIMITER //
CREATE PROCEDURE getList
(
  IN uId INT,
  IN lId INT
)
/*  Collaborations identifies all lists that a particular user has access to.
 *  Each list identifies it's owner.
 */
BEGIN
   SELECT U.userId AS 'ownerId', U.userName AS 'ownerName',
      L.listId, L.listName, L.listDescription, L.listSince,
      C.accessType, C.collaborationViewed, C.collaboratorSince
      FROM lists AS L,
        collaborators AS C,
        users AS U
      WHERE C.listId = L.listId AND
        L.userId = U.userId AND
        C.userId = uId AND
        C.listId = lId;
END //
DELIMITER ;
