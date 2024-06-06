#!/usr/bin/python3


def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    keys = set(boxes[0])
    opened_boxes = {0}

    while True:
        new_keys = keys.copy()
        for i in range(n):
            if i in keys and i not in opened_boxes:
                new_keys.update(boxes[i])
                opened_boxes.add(i)

        if new_keys == keys:
            break

        keys = new_keys

    return len(opened_boxes) == n
