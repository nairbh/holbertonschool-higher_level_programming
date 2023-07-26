-- Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa
USE hbtn_0d_usa;
SELECT cities.id, cities.name AS my_CITY, states.name AS my_state_name FROM cities, states WHERE cities.states_id = states.id AND states.name = 'California' ORDER BY cities.id ASC;
