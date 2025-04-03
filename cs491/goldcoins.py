def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    w = int(next(it))
    h = int(next(it))
    k = int(next(it))
    c = int(next(it))
    
    grid = [[0] * (h + 1) for _ in range(w + 1)]
    

    for _ in range(n):
        x = int(next(it))
        y = int(next(it))
        grid[x][y] += 1


    for i in range(w + 1):
        for j in range(h + 1):
            if i > 0:
                grid[i][j] += grid[i-1][j]
            if j > 0:
                grid[i][j] += grid[i][j-1]
            if i > 0 and j > 0:
                grid[i][j] -= grid[i-1][j-1]
                
    max_profit = 0
    for a in range(w + 1):
        for b in range(h + 1):
            coins = grid[a][b]
            profit = k * coins - c * (a * b)
            if profit > max_profit:
                max_profit = profit
    
    sys.stdout.write(str(max_profit))

if __name__ == "__main__":
    main()
