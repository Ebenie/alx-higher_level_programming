-- This command lists all shows from the hbtn_0d_tvshows_rate
--  database by their rating.
-- It selects the title of each show along with the sum of its
-- ratings, calculates the sum of ratings using the SUM() function,
--  groups the results by the show's title using GROUP BY, and
-- finally sorts the results in descending order by the rating sum.

SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating DESC;
