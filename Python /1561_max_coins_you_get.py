# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
def maxCoins(piles):
    sorted_piles = sorted(piles)
    left = 0
    right = len(sorted_piles) - 1
    triplets = []
    while left < right:
        triplet = []
        triplet.append(sorted_piles[left])
        triplet.append(sorted_piles[right])
        triplet.append(sorted_piles[right-1])
        left += 1
        right -= 2
        triplets.append(triplet)
            
    our_max_coins = 0
    for triplet in triplets:
        our_max_coins += triplet[2]
    return our_max_coins
            
            
            
print(maxCoins([9,8,7,6,5,1,2,3,4]))
