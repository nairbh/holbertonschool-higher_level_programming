#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if not isinstance(roman_string, str) or not roman_string:
        return 0

    if len(roman_string) == 1:
        return roman.get(roman_string, 0)

    first = roman.get(roman_string[0], 0)
    second = roman.get(roman_string[1], 0)

    if first >= second:
        return first + roman_to_int(roman_string[1:])
    else:
        return second - first + roman_to_int(roman_string[2:])
