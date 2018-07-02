CREATE TABLE items
(
    itemId INT NOT NULL AUTO_INCREMENT,
    itemPosition INT NOT NULL DEFAULT 1,
    itemName VARCHAR(255),
    itemDetail VARCHAR(255),
    completed BOOLEAN DEFAULT false,
    listId INT NOT NULL,
    creatorId INT NOT NULL,
    itemSince  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (itemId),
    FOREIGN KEY (listId)
            REFERENCES lists(listId)
            ON DELETE CASCADE
);
