#!/usr/bin/python3

"""Creating a function that can efficiently determine if all boxes can be opened
"""


def canUnlockAll(boxes):
    """
    defining the canUnlockAll function that determines if all the boxes can be opened
    Args:
        boxes (list of lists): A 2D list representing the boxes and their keys
    """
    # Initializing a set to keep track of unlocked boxes
    unlocked = set()
    queue = [0]
    
    while queue:
        # current box index
        current = queue.pop(0)
        if current in unlocked:
            continue
        # Mark the current box as unlocked
        unlocked.add(current)
        # Add keys from the current box to the queue if they unlock new boxes
        for key in boxes[current]:
            if key not in unlocked and key < len(boxes):
                queue.append(key)
    
    # Checking if the number of unlocked boxes is equal to the total number of boxes
    return len(unlocked) == len(boxes)