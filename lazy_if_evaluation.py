"""
As in most programming languages, Python's if is lazily evaluated. This means that in: if x and y, condition y will not
be tested if x is already False. We can exploit this by checking a fast condition first before checking a slow condition

For example, say we are looking for abbreviations in text:
"""

abbreviations = ['cf.', 'e.g.', 'ex.', 'etc.', 'fig.', 'i.e.', 'Mr.', 'vs.']

for n in range(1000000):
    for w in ('Mr.', 'Hat', 'is', 'chasing', 'the', 'black', 'cat', '.'):
        if w in abbreviations:
            pass  # Process abbreviation here.

"""
The algorithm takes 4.3 seconds to run. However, since most of the words are not abbreviations we can optimize it by 
first checking if a word ends with a period, which is faster than iterating the list of known abbreviations:

Now it takes 3.1 seconds to run, a x1.4 speedup.
"""
for n in range(1000000):
    for w in ('Mr.', 'Hat', 'is', 'chasing', 'the', 'black', 'cat', '.'):
        if w[-1] == '.' and w in abbreviations:
            pass
