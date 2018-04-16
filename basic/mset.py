basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

g = 'orange' in basket                 # fast membership testing
print(g)
h = 'crabgrass' in basket
print(h)

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print(a)                                  # unique letters in a

a1 = a - b                              # letters in a but not in b
print(a1)
a2 = a | b                              # letters in a or b or both
print(a2)
a3 = a & b                              # letters in both a and b
print(a3)
a4 = a ^ b                              # letters in a or b but not both
print(a4)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a) 