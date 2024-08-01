#!/usr/bin/python3
"""
Lockboxes Problem
"""

def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be opened.
    """

    n = len(boxes)
    checked = set([0])
    unchecked = set(boxes[0]).difference(set([0]))
    while len(unchecked) > 0:
        i = unchecked.pop()
        if not i or i >= n or i < 0:
            continue
        if i not in checked:
            unchecked = unchecked.union(boxes[i])
            checked.add(i)
    return n == len(checked)
