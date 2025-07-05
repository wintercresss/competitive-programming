from collections import deque

def min_knight_moves(start_r, start_c, tgt_r, tgt_c, n):
    # this code assumes board size/indexing of [0...n-1] inclusive
    if start_r < 0 or start_c < 0 or start_r >= n or start_c >= n:
        return -1
    if tgt_r < 0 or tgt_c < 0 or tgt_r >= n or tgt_c >= n: # return -1 if either start or target is out of bounds
        return -1

    queue = deque([(start_r, start_c)])
    visited = {(start_r, start_c)}
    previous = dict()
    directions = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    while queue:
        curr_r, curr_c = queue.popleft()
        if curr_r == tgt_r and curr_c == tgt_c:
            path_taken = [(curr_r, curr_c)]
            while (curr_r, curr_c) in previous: # reconstruct path, starting from the target and going until we are back at the start. our start has no previous, so it will stop there.
                path_taken.append(previous[(curr_r, curr_c)])
                curr_r, curr_c = previous[(curr_r, curr_c)]
            path_taken = path_taken[::-1] # reverse, since we we reconstructed the path in reverse order
            return path_taken

        for change_x, change_y in directions:
            next_r, next_c = curr_r + change_x, curr_c + change_y
            if next_r < 0 or next_c < 0 or next_r >= n or next_c >= n or (next_r, next_c) in visited:
                continue
            previous[(next_r, next_c)] = (curr_r, curr_c)
            visited.add((next_r, next_c))
            queue.append((next_r, next_c))
    
    return -1 # not possible, return -1

def visualize_path(start_r, start_c, tgt_r, tgt_c, n):
    # this assumes that (0, 0) is the top left of the board, and (n-1, n-1) is the bottom right
    path = min_knight_moves(start_r, start_c, tgt_r, tgt_c, n)
    if path == -1:
        print("no path found!!")
        return
    for i in range(n):
        for j in range(n):
            if i == start_r and j == start_c:
                print("N", end="  ")
            elif i == tgt_r and j == tgt_c:
                print("T", end="  ")
            elif (i, j) in path:
                print(path.index((i, j)), end="  ") # assuming 0-indexing when counting the nth square in the path
            else:
                print("-", end="  ")
        print("\n")


print("Path from (0, 0) to (5, 5) in a 6x6 board")
print(min_knight_moves(0, 0, 5, 5, 6))
visualize_path(0, 0, 5, 5, 6)

print("Path from (0, 0) to (7, 4) in a 8x8 board")
print(min_knight_moves(0, 0, 7, 4, 8))
visualize_path(0, 0, 7, 4, 8)

print("Path from (0, 0) to (7, 0) in a 8x8 board")
print(min_knight_moves(0, 0, 7, 0, 8))
visualize_path(0, 0, 7, 0, 8)

# edge cases:
assert min_knight_moves(-1, -1, 1, 1, 0) == -1     # return -1 if starting is out of bounds
assert min_knight_moves(1, 1, -1, 1, 1) == -1      # return -1 if the target is out of bounds
assert min_knight_moves(0, 0, 0, 0, 1) == [(0, 0)] # returns just the starting position if the start and end are the exact same
assert min_knight_moves(0, 0, 1, 1, 1) == -1       # going from (0, 0) to (1, 1) in a 1x1 board is impossible! ensure that this is the case