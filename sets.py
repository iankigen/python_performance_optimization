"""
Sets
Set operations (union, intersection, difference) are faster than iterating over lists:

Syntax	Operation	Description
set(list1) | set(list2)	union	New set with values from both list1 and list2.
set(list1) & set(list2)	intersection	New set with values common to list1 and list2.
set(list1) - set(list2)	difference	New set with values in list1 but not in list2.
You can use them to merge two lists, or to make a list of unique values for example.
"""

print(list(set([1, 2, 2, 3])))
print(list(set([1, 2]) | set([2, 3])))
print(list(set([1, 2]) & set([2, 3])))