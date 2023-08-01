#!/usr/bin/python3
""" write a script that lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit("Usage: file_name, username, password, db, state_name")

    username, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id", (state_name,))
        for row in cur.fetchall():
            print(row)
    conn.close()
