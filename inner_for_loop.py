"""
Inner for-loops
If your code has nested for-loops, all optimizations inside the inner loop count. Consider the following
The algorithm takes 4.0 seconds to run. It is a hypothetical example, but the point is this: we can make it faster by
moving v1[i] outside of the inner loop:
"""

v1 = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0] * 10
v2 = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0] * 10

for n in range(1000):
    for i in range(len(v1)):
        for j in range(len(v2)):
            x = v1[i] + v2[j]

"""
Now it takes 3.2 seconds to run. In the first example, v1[i] is called  100 x 100 x 100 = 1,000,000 times. In this 
example, we look up number i in v1 once before iterating over v2, so v1[i]  is called only 100 x 100 times, making the 
algorithm x1.3 faster. Move everything you can outside of the inner loop.
"""
for n in range(1000):
    for i in range(len(v1)):
        v1i = v1[i]
        for j in range(len(v2)):
            x = v1i + v2[j]
