# Problem Statement: https://www.hackerrank.com/challenges/sparse-arrays/problem
def matchingStrings(strings, queries):
    # Write your code here
    ans = []
    for query in queries:
        count = 0
        for string in strings:
            if query == string:
                count += 1
        ans.append(count)
    return ans
  
  
  print(matchingStrings(['ab','ab', 'abc'],['ab','abc','bc']))
