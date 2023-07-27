CREATE DATABASE IF NOT EXISTS hbtn_0d_tvshows;
USE hbtn_0d_tvshows;

CREATE TABLE IF NOT EXISTS genres (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

INSERT INTO genres (id, name) VALUES
    (1,'Drama'),
    (2, 'Thriller'),
    (3, 'Fantasy'),
    (4, 'Mystery'),
    (5, 'Comedy');

CREATE TABLE IF NOT EXISTS title (
    title VARCHAR(256) NOT NULL,
    genre_id INT NOT NULL,
    FOREIGN (title, genre_id) REFERENCE (genres.id)
);

INSERT INTO title (title, genre_id) VALUES
    ('Breaking Bad', 1),
    ('Breaking Bad', 1),
    ('Breaking Bad', 1),
    ('Breaking Bad', 1),
    ('Dexter', 1),
    ('Dexter', 2),
    ('Dexter', 2),
    ('Dexter', 2),
    ('Dexter', 3),
    ('Game of Thrones', 1),
    ('Game of Thrones', 3),
    ('Game of Thrones', 4),
    ('House', 1),
    ('House', 2),
    ('New Girl', 5),
    ('Silicon Valley', 5),
    ('The Big Bang Theory', 5),
    ('The Last Man on Earth', 1),
    ('The Last Man on Earth', 5);

