

"creating a funtiong returns the perimeter of the island described in grid"


def island_perimeter(grid):
    """
    defining the island_perimeter funtion that \ 
    returns the perimeter of the island described in grid:

    Args:
    grid (list): 0 represents a water zone
                1 represents a land zone
                One cell is a square with side length 1
                Grid cells are connected horizontally/vertically (not diagonally).
                Grid is rectangular, width and height don’t exceed 100
    """
    perim = 0

    for i in range(len(grid)):
        for k in range(len(grid[0])):
            if grid[i][k] == 1:
                perim += 4
                if (i > 0 and grid[i - 1][k] == 1):
                    perim -= 2
                if (k > 0 and grid[i][k - 1] == 1):
                    perim -= 2
    return perim



grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]

print(island_perimeter(grid))
            
            


