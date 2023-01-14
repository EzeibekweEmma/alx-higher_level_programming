#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        score = 0
        name = ""
        for x in a_dictionary:
            if score < a_dictionary[x]:
                name = x
                score = a_dictionary[x]
            else:
                continue

        return name
    else:
        return None
