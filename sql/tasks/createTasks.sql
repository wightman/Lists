CREATE TABLE tasks
(
    taskId INT NOT NULL AUTO_INCREMENT,
    taskPosition INT NOT NULL DEFAULT 1,
    task VARCHAR(255),
    completed BOOLEAN DEFAULT false,
    listId INT NOT NULL,
    taskSince  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (taskId),
    FOREIGN KEY (listId)
            REFERENCES lists(listId)
            ON DELETE CASCADE
);
