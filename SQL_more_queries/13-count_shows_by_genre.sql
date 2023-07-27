-- Import the database dump from hbtn_0aaaaad_tvshows to your MySQL server: download (same as 11-genre_id_all_shows.sql

SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
SELECT tv_genres.name, count(*) AS number_of_shows FROM tv_genres JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY tv_genres.name ORDER BY tv_genres.id DESC;
