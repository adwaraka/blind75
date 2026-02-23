# Gas Station
# https://algo.monster/liteproblems/134

def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    n = len(gas)
    ptr1, ptr2 = n - 1, n - 1  # ptr1 will move back, ptr2 forward
    gasBalance = 0  # how much gas is left
    stationsVisited = 0

    while stationsVisited < n:
        gasBalance += gas[ptr2] - cost[ptr2]
        stationsVisited+=1
        ptr2 = (ptr2 + 1) % n

        # if gas is not sufficient and all stations not visited
        while gasBalance < 0 and stationsVisited < n:
            ptr1 = (ptr1 - 1 + n) % n  # required for ptr1 to rotate correctly
            gasBalance += gas[ptr1] - cost[ptr1]
            stationsVisited+=1

    if gasBalance >= 0:
        return ptr1
    else:
        return -1

# better solution
def canCompleteCircuit2(gas: list[int], cost: list[int]) -> int:
    if sum(gas) < sum(cost):
        return -1

    n = len(gas)
    start = 0
    currentGas = 0

    # this loop is to find the correct index
    for i in range(n):
        currentGas += gas[i] - cost[i]
        # we have run out of gas
        if currentGas < 0:
            currentGas = 0
            start = i + 1

    return start


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(canCompleteCircuit(gas, cost))
print(canCompleteCircuit2(gas, cost))
