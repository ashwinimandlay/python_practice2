# combination module
from itertools import combinations
# format is same as permutation from itertools
# combination(list, length)

print(list(combinations('1234', 3)))

# IMPORTANT NOTE: for repeatability
# import combination_with_replacement

from itertools import combinations_with_replacement
print(list(combinations_with_replacement('1234', 3)))
