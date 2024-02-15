-- This command lists all genres in the hbtn_0d_tvshows_rate 
-- database by their rating.
-- It selects the genre name along with the sum of ratings
-- for shows in each genre, calculates the sum of ratings using
-- the SUM() function, groups the results by the genre name using GROUP BY,
-- and finally sorts the results in descending order by the rating sum.

SELECT tv_genres.name, SUM(rating) AS rating
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;

