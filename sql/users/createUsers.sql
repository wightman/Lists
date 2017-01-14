CREATE TABLE users
(
    userId INT NOT NULL AUTO_INCREMENT,
    userName VARCHAR(255) UNIQUE NOT NULL,
    userPassword VARCHAR(255) NOT NULL,
    userAdmin BOOLEAN DEFAULT false,
    PRIMARY KEY (userId)
);
