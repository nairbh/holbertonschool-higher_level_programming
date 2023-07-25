-- Write a script that creates the database hbtn_0d_2 and the user user_0d_2.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
USE hbtn_0d_2;

DELIMITER //
CREATE PROCEDURE create_user_if_not_exists()
BEGIN
    DECLARE user_exists INT DEFAULT 0;

    SELECT COUNT(*) INTO user_exists FROM mysql.user WHERE user = 'user_0d_2' AND host = 'localhost';

    IF user_exists = 0 THEN
        CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
        GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
    END IF;
END //
DELIMITER ;

CALL create_user_if_not_exists();
DROP PROCEDURE IF EXISTS create_user_if_not_exists;
FLUSH PRIVILEGES;
