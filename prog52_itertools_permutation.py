# >>> from itertools import permutations
# format is: permutation(list or string, length)
# if no length is mentioned it takes len(list or string)

# >>> print permutations(['1','2','3'])
# <itertools.permutations object at 0x02A45210>
# therefore we must make it a list or set

# >>>
# >>> print list(permutations(['1','2','3']))
# here length is 3
# [('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]

# >>>
# >>> print list(permutations(['1','2','3'],2))
# length is 2 here
# [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]

# >>>
# >>> print list(permutations('abc',3))
# [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
