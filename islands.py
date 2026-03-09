from collections import deque

def islandsAndTreasure(grid: list[list[int]]) -> None:
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    q = deque()

    def addCell(r, c):
        if 0 <= r < ROWS and 0 <= c < COLS and (r, c) not in visit and grid[r][c] != -1:
            visit.add((r, c))
            q.append([r, c])

    # the ones with the treasure chest is already present
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 0:
                q.append([r, c])
                visit.add((r, c))

    dist = 0
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            grid[r][c] = dist
            addCell(r + 1, c)
            addCell(r - 1, c)
            addCell(r, c + 1)
            addCell(r, c - 1)
        dist += 1
    print(grid)


grid = [
    [2147483647,-1,0,2147483647],
    [2147483647,2147483647,2147483647,-1],
    [2147483647,-1,2147483647,-1],
    [0,-1,2147483647,2147483647]
]
islandsAndTreasure(grid)