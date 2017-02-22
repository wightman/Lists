CREATE TABLE collaborators
(
    userId INT NOT NULL,
    listId INT NOT NULL,
    access CHAR(1),
    collaboratorSince  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT collaboratorUser FOREGIN KEY userID REFERENCES users(userID)
        ON DELETE CASCADE,
    CONSTRAINT collaboratorList FOREGIN KEY access REFERENCES lists(listID)
        ON DELETE CASCADE,
    CONSTRAINT collaboratorAccess FOREGIN KEY access REFERENCES access(access)
);

CREATE TABLE access
(
   access CHAR(1) UNIQUE
);

INSERT INTO access ('R');
INSERT INTO access ('W');
