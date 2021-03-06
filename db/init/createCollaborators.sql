CREATE TABLE accessTypes
(
   access CHAR(1) UNIQUE
);

INSERT INTO accessTypes (access) VALUES ('R');
INSERT INTO accessTypes (access) VALUES ('W');
INSERT INTO accessTypes (access) VALUES ('O');

CREATE TABLE collaborators
(
    userId INT NOT NULL,
    listId INT NOT NULL,
    accessType CHAR(1) NOT NULL,
    collaborationViewed BOOLEAN DEFAULT FALSE,
    collaboratorSince TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (userId)
        REFERENCES users(userId)
        ON DELETE CASCADE,
    FOREIGN KEY (listId)
        REFERENCES lists(listId)
        ON DELETE CASCADE,
    FOREIGN KEY (access)
        REFERENCES accessTypes(access),
    UNIQUE KEY collaboratorList (userId, listId)
);
