from itertools import permutations      #there exists a tool already

perm = permutations(input())

for i in list(perm): 
    print(i)

"""
with input of "abc" the output is:
('a', 'b', 'c')
('a', 'c', 'b')
('b', 'a', 'c')
('b', 'c', 'a')
('c', 'a', 'b')
('c', 'b', 'a')
"""