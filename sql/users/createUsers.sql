CREATE TABLE users
(
    userId INT NOT NULL AUTO_INCREMENT,
    userName VARCHAR(255) NOT NULL,
    userEmail VARCHAR(255) UNIQUE NOT NULL
    userPassword BINARY(60) NOT NULL, --BCrypted
    userAdmin BOOLEAN DEFAULT false,
    userSince TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (userId)
);
/* http://dba.stackexchange.com/questions/20217/mysql-set-utc-time-as-default-timestamp
   and in particular setting the default for the database:
   [mysqld]
   **other variables**
  default_time_zone='+00:00'
 */
