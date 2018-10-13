DELIMITER //
CREATE PROCEDURE getLists
(
  IN uId INT
)
/*  Collaborations identifies all lists that a particular user has access to.
 *  Each list identifies it's owner.
 */
BEGIN
   SELECT U.userId AS 'OwnerId', U.userName AS 'ownerName',
      L.listId, L.listName, L.listDescription, L.listSince,
      C.accessTypes, C.collaborationViewed, C.collaboratorSince
      FROM lists AS L,
        collaborators AS C,
        users AS U
      WHERE C.listId = L.listId AND
        L.userId = U.userId AND
        C.userId = uId;
END //
DELIMITER ;
