n = int(input())
board = [input().strip() for _ in range(n)]

directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
n = len(board)
longest_sequence = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == 'X':
            for dx, dy in directions:
                x = i
                y = j
                count = 0
                while 0 <= x < n and 0 <= y < n and board[x][y] == 'X':
                    x += dx
                    y += dy
                    count += 1
                longest_sequence = max(longest_sequence, count)

print(longest_sequence)
