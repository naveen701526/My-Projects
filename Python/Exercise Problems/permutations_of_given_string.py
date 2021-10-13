from itertools import product
def all_repeat(str1, rno):
  chars = list(str1)
  results = []
  for c in product(chars, repeat = rno):
    results.append(c)
  return results
print(all_repeat('xyz', 3))
print(all_repeat('xyz', 2))
print(all_repeat('abcd', 4))
