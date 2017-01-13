CREATE TABLE tasks
(
    taskId INT NOT NULL AUTO_INCREMENT,
    task VARCHAR(255),
    completed BOOLEAN DEFAULT false,
    listId INT NOT NULL,

    PRIMARY KEY (taskId),
    FOREIGN KEY (listId)
            REFERENCES lists(listId)
            ON DELETE CASCADE
);
