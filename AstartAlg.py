from copy import deepcopy
import numpy as np
import time


def bestsolution(state):
    bestsol = np.array([], int).reshape(-1, 9)
    count = len(state) - 1

    while count != -1:
        bestsol = np.insert(bestsol, 0, state[count]['puzzle'], 0)
        count = state[count]['parent']

    return bestsol.reshape(-1, 3, 3)


def misplaced_tiles(puzzle, goal):
    mscost = np.sum(puzzle != goal) - 1

    if mscost > 0:
        return mscost
    else:
        return 0


def coordinates(puzzle):
    pos = np.array(range(9))

    for p, q in enumerate(puzzle):
        pos[q] = p

    return pos


def evaluvate_misplaced(puzzle, goal):

    steps = [
        ('up', [0, 1, 2], -3),
        ('down', [6, 7, 8], 3),
        ('left', [0, 3, 6], -1),
        ('right', [2, 5, 8], 1)
    ]

    dtstate = [
        ('puzzle', list),
        ('parent', int),
        ('gn', int),
        ('hn', int)
    ]

    costg = coordinates(goal)

    parent = -1
    gn = 0
    hn = misplaced_tiles(
        coordinates(puzzle),
        costg
    )

    state = np.array(
        [(puzzle, parent, gn, hn)],
        dtype=dtstate
    )

    dtpriority = [
        ('position', int),
        ('fn', int)
    ]

    priority = np.array(
        [(0, hn)],
        dtype=dtpriority
    )

    start_time = time.time()

    while len(priority) > 0:

        priority = np.sort(
            priority,
            kind='mergesort',
            order=['fn', 'position']
        )

        position, fn = priority[0]

        priority = np.delete(priority, 0, 0)

        puzzle, parent, gn, hn = state[position]

        puzzle = np.array(puzzle)

        # Find the position of blank tile (0)
        blank = np.where(puzzle == 0)[0][0]

        gn = gn + 1

        for move, invalid_positions, head in steps:

            if blank not in invalid_positions:

                openstates = deepcopy(puzzle)

                new_position = blank + head

                # Swap blank with tile
                openstates[blank], openstates[new_position] = (
                    openstates[new_position],
                    openstates[blank]
                )

                # Check whether state already exists
                exists = False

                for old_state in state['puzzle']:
                    if np.array_equal(old_state, openstates):
                        exists = True
                        break

                if not exists:

                    hn = misplaced_tiles(
                        coordinates(openstates),
                        costg
                    )

                    q = np.array(
                        [(openstates.tolist(), position, gn, hn)],
                        dtype=dtstate
                    )

                    state = np.append(
                        state,
                        q,
                        axis=0
                    )

                    fn = gn + hn

                    q = np.array(
                        [(len(state) - 1, fn)],
                        dtype=dtpriority
                    )

                    priority = np.append(
                        priority,
                        q,
                        axis=0
                    )

                    # Check goal
                    if np.array_equal(openstates, goal):

                        print("The 8 puzzle is solvable\n")

                        return state, len(priority)

        # Stop if execution takes too long
        if time.time() - start_time > 2:

            print("The 8 puzzle is unsolvable\n")

            return state, len(priority)

    return state, len(priority)


puzzle = [
    2, 8, 3,
    1, 6, 4,
    7, 0, 5
]
goal = [
    1, 2, 3,
    8, 0, 4,
    7, 6, 5
]
state, visited = evaluvate_misplaced(
    puzzle,
    goal
)
bestpath = bestsolution(state)

print(
    str(bestpath)
    .replace('[', ' ')
    .replace(']', '')
)

totalmoves = len(bestpath) - 1

print("\nSteps to reach goal:", totalmoves)

visit = len(state) - visited

print("Total nodes visited:", visit)
