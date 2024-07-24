#!/usr/bin/python3
"""define function add rwo integers"""

#!/usr/bin/python3
"""
This module is documented
"""

def add_integer(a, b = 98):
    """Add two integers
    >>> add_integer(1, 2)
    3
    >>> add_integer(3, 4)
    7
    """
    if (not isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    elif (not isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    return int(round(a)) + int(round(b))
