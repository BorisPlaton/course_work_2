CREATE USER 'kirill_panchenko'@'localhost' IDENTIFIED BY 'qwerty';
GRANT ALL PRIVILEGES ON course_work.* TO 'kirill_panchenko'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;