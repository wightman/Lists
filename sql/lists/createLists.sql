CREATE TABLE lists
(
    listId INT NOT NULL AUTO_INCREMENT,
    listName VARCHAR(255) NOT NULL,
    userId INT NOT NULL,

    PRIMARY KEY (listId),
    FOREIGN KEY (userId)
            REFERENCES users(userId)
            ON DELETE CASCADE,
     UNIQUE KEY listIdName ( userId, listName)
);
