#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa  """

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    with conn.cursor() as cur:
        sql_inject = "SELECT cities.id, cities.name, states.name \
                 FROM cities \
                 INNER JOIN states \
                 ON states.id = cities.state_id \
                 WHERE states.name = %s \
                 ORDER BY cities.id"

        cur.execute(sql_inject, (sys.argv[4],))

        cities_in_state = cur.fetchall()

        for city in cities_in_state:
            print(', '.join([row[1] for row in cities_in_state]))

    conn.close()
