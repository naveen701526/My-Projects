# https://leetcode.com/problems/minimum-index-sum-of-two-lists/
def findRestaurant(list1, list2):
    common_parts= list((set(list1)).intersection(set(list2)))
    candidates = {}
    output = []
    min_val = 10000
    for common in common_parts:
        candidates[common] = list1.index(common) + list2.index(common)
        if list1.index(common) + list2.index(common) < min_val:
            min_val = list1.index(common) + list2.index(common)
    for candidate in candidates:
        if candidates[candidate] == min_val:
            output.append(candidate)
    return output
            
print(findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],
["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
