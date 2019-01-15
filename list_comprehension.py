"""
List comprehensions are faster than building a new list in a for-loop. The first example below uses a loop and takes 6.6
seconds. The second example uses list comprehension and takes 5.3 seconds, a x1.2 speedup.
"""

words = ['Mr.', 'Hat', 'is', 'feeding', 'the', 'black', 'cat', '.']
for n in range(1000000):
    a = []
    for w in words:
        if w != '.':
            a.append(w.lower())

for n in range(1000000):
    a = [w.lower() for w in words if w != '.']
