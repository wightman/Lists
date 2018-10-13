DELIMITER //
CREATE PROCEDURE getListsByAccess
(
  IN uId INT,
  IN aType CHAR
)
/*  Collaborations identifies all lists that a particular user has access to.
 *  Each list identifies it's owner.
 */
BEGIN
   SELECT U.userId AS 'OwnerId', U.userName AS 'ownerName',
      L.listId, L.listName, L.listDescription, L.listSince,
      C.accessType, C.collaborationViewed, C.collaboratorSince
      FROM lists AS L,
        collaborators AS C,
        users AS U
      WHERE C.listId = L.listId AND
        L.userId = U.userId AND
        C.userId = uId AND
        C.accessType = aType;
END //
DELIMITER ;
