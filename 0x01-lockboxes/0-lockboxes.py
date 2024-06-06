#!/usr/bin/python3


def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    keys = set(boxes[0])

    for i in range(n):
        if i in keys:
            keys.update(boxes[i])

    return len(keys) == n
