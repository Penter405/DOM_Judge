from collections import Counter
d=min(list(zip(*Counter("TTTAAA").most_common()))[0])
print(d)
