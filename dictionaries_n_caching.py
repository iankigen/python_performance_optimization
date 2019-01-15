"""
Here is a comparison of four implementations of the cosine distance algorithm, which measures similarity between vectors
of features (words) with feature weights (word relevance). The first implementation represents vectors as ordered,
equal-length lists of feature weights. The second represents vectors as sparse dictionaries of feature → weight items,
where features with weight = 0 are omitted. The third subclasses a dictionary and uses caching for l2(). The fourth adds
a distance cache.
"""


#  The first implementation takes 1.5 seconds to run (and more for longer vectors):

def distance(v1, v2):
    return sum(w1 * w2 for w1, w2 in zip(v1, v2)) / (l2(v1) * l2(v2) or 1)


def l2(v):
    return sum(w ** 2 for w in v) ** 0.5


for i in range(100000):
    d = distance([2, 1, 1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 3, 1])


# To make it faster we can cache the costly L2-norm math, since it always yields the same result for a given vector.
# The third implementation then takes 0.6 seconds, a x2.5 speedup:

class Vector(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        self.l2 = sum(w ** 2 for w in self.values()) ** 0.5


def distance(v1, v2):
    return sum(v1[f] * v2.get(f, 0) for f in v1) / (v1.l2 * v2.l2 or 1)


for i in range(100000):
    d = distance(Vector({0: 2, 1: 1, 2: 1}), Vector({0: 1, 8: 3, 9: 1}))

"""
Finally, we cache the distances. Python's id() function returns a unique id for each object. When we calculate the 
distance between v1 and v2, we can store the result in a global CACHE dictionary, under CACHE[(id(v1),id(v2))] – since 
keys must be hashable we can't use (v1,v2) directly.

Next time, we can check if the result is already in the cache – a dictionary lookup is faster than the math.

This ensures that calculating distance is never more than O(n*n) for n vectors. 

"""

CACHE = {}


def distance(v1, v2):
    k = id(v1), id(v2)
    if k not in CACHE:
        d = sum(v1[f] * v2.get(f, 0) for f in v1) / (v1.l2 * v2.l2 or 1)
        CACHE[k] = d
        CACHE[id(v2), id(v1)] = d  # symmetric
    return CACHE[k]
