#!/usr/bin/python3
# Write a script that lists all State objects from the database hbtn_0e_6_usa

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

username, password, db = sys.argv[1], sys.argv[2], sys.argv[3]
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(username, password, db))
Session = sessionmaker(bind=engine)
session_encap = Session()

results = session_encap.query(State).order_by(State.id).all()

for state in results:
    print("{}: {}".format(state.id, state.name))

session_encap.close()
