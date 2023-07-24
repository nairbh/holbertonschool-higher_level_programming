--  that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.
select score, name from second_table
where score >=10 order by score desc;
