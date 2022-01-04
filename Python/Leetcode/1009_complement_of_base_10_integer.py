class Solution:
    def bitwiseComplement(self, n: int) -> int:
        res = 0
        complement = []

        # handle corner case
        if n == 0:
            return 1

        # update complement list with complement of each digit in reverse order
        while n > 0:
            if n & 1 == 0:
                complement.append(1)
            else:
                complement.append(0)
            n >>= 1

        # obtain the result in decimal format
        for i, c in enumerate(complement):
            res += pow(2, i) * c

        return res
