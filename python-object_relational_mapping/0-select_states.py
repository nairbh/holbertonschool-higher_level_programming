
#!/usr/bin/python3
import sys
import MySQLdb


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("Use: file_name, username, passeword, db ")
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], password=sys.argv[2], database=sys.argv[3], charset="utf8")    
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        for row in cur.fetchall():
            print(cur)
    cur.close()
    conn.close()