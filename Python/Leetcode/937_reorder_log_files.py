import heapq


class Solution:

    def reorderLogFiles(self, logs):

        let = []
        dig = []
        heap = []

        for log in logs:
            res = log.split(' ')
            if res[1][0].isdigit():
                dig.append(log)
                continue
            cont = ' '.join(res[1:])
            iden = res[0]
            # we will heapify by lexicographical order of content then identifier
            heapq.heappush(heap, (cont, iden))

        for _ in range(len(heap)):
            # heappop gives the lexicographically smallest element
            cont, iden = heapq.heappop(heap)
            let.append(iden + ' ' + cont)

        return let + dig
