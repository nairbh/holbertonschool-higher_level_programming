#!/usr/bin/python3
def best_score(a_diction):
    if not a_diction:
        return None

    max_key = max(a_diction, key=a_diction.get)
    return max_key
