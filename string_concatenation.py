"""
String concatenation
Format strings are often faster than concatenating values to strings:
"""

s = '<feature term="' + 'cat' + '" weight="' + str(1.0) + '" />'

s = '<feature term="%s" weight="%s" />' % ('cat', 1.0)  # Faster format string.

"""
If you are constructing a large string (for example, XML output), it is faster to append the different parts to a list
and collapse it at the end:
"""

features = [('cat', 1.0), ('dog', 0.0)]

xml = []
for term, weight in features:
    xml.append('<feature term="%s" weight="%s" />' % (term, weight))
print(xml)
xml = '\n'.join(xml)
print(xml)
