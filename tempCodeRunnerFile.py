    grid = [[0, 1],
            [1, 0]]                         # Output: 1
    print(sol.shortestBridge(grid))

    grid = [[0, 1, 0],
            [0, 0, 0],
            [0, 0, 1]]                      # Output: 2
    print(sol.shortestBridge(grid))

    grid = [[1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]]                # Output: 1
    print(sol.shortestBridge(grid))