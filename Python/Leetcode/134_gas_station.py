class Solution:

    def forwarding(self, stops: list, costs: list, length: int):
        # var reservation
        tank = 0
        # enumerate
        for var in range(length):
            tank += stops[var] - costs[var]
            if tank < 0:
                return var
        return True

    def canCompleteCircuit(self, stops, costs):
        # check if impossible to achieve significantly
        if sum(stops) < sum(costs):
            return -1

        # var reservation
        driving, length = 0, len(costs)
        # validate by each start`1````
        while driving < length:
            # if start fill can not converage cost, step forward
            if stops[driving] < costs[driving]:
                driving += 1
                continue
            # re-create route sequence
            add, use = stops[driving:] + stops[:driving +
                                               1], costs[driving:] + costs[:driving + 1]
            x = self.forwarding(add, use, length)
            if type(x) == int:
                driving += x
            else:
                return driving

        # catch infeasible
        return -1
