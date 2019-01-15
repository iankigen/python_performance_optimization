"""
Regular expressions in Python are fast because they are pushed back to C code. However, in many situations simple string
methods are even faster. Below is a list of interesting string methods. If you do use regular expressions, remember to
add source code comments what they do.


Method	Description
str[-1] == 'x'	True if the last character is "x" (but Exception if len(str) == 0).
str.isalpha()	True if the string only contains a-z | A-Z characters.
str.isdigit()	True if the string only contains 0-9 characters.
str.startswith(('x', 'yz'))	True if the first characters in the string are "x" or "yz".
str.endswith(('x', 'yz'))	True if the last characters in the string are "x" or "yz".
"""

