"""
If + None
`if done is not None` is faster than `if done != None`, which in turn is faster than `if not done`.
It's nitpicking but it matters inside inner loops.
"""