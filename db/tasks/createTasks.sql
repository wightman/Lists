CREATE TABLE tasks
(
    taskId INT NOT NULL AUTO_INCREMENT,
    taskPosition INT NOT NULL DEFAULT 1,
    taskName VARCHAR(255),
    taskDetail VARCHAR(255),
    completed BOOLEAN DEFAULT false,
    listId INT NOT NULL,
    creatorId INT NOT NULL,
    taskSince  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (taskId),
    FOREIGN KEY (listId)
            REFERENCES lists(listId)
            ON DELETE CASCADE
);
