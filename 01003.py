power = int(input())
if 1 <= power <= 8:
    size = 2 ** power
    empty = input().split(" ")
    ey = int(empty[0]) - 1
    ex = int(empty[1]) - 1
    board = [[None] * size for i in range(size)]
    board[ey][ex] = "*"

    def function(h, x, y, a, b, d):
        #top left
        if h == 1:
            if d == 1 or d == 4:
                char = "a"
            elif d == 2 or d == 3:
                char = "e"
            #top left
            if x < a and y < b:
                board[b][a-1], board[b-1][a], board[b][a] = char, char, char
            #top right
            elif x >= a and y < b:
                board[b-1][a-1], board[b][a-1], board[b][a] = char, char, char
            #bottom left
            elif x < a and y >= b:
                board[b-1][a-1], board[b-1][a], board[b][a] = char, char, char
            #bottom right
            elif x >= a and y >= b:
                board[b-1][a-1], board[b][a-1], board[b-1][a] = char, char, char

        else:
            half = int(h/2)

            #top left
            if x < a and y < b:
                board[b][a-1], board[b-1][a], board[b][a] = "o", "o", "o"
                function(half, x, y, a-half, b-half, 1)
                function(half, a, b-1, a+half, b-half, 2)
                function(half, a-1, b, a-half, b+half, 3)
                function(half, a, b, a+half, b+half, 4)
            #top right
            elif x >= a and y < b:
                board[b-1][a-1], board[b][a-1], board[b][a] = "o", "o", "o"
                function(half, a-1, b-1, a-half, b-half, 1)
                function(half, x, y, a+half, b-half, 2)
                function(half, a-1, b, a-half, b+half, 3)
                function(half, a, b, a+half, b+half, 4)
            #bottom left
            elif x < a and y >= b:
                board[b-1][a-1], board[b-1][a], board[b][a] = "o", "o", "o"
                function(half, a-1, b-1, a-half, b-half, 1)
                function(half, a, b-1, a+half, b-half, 2)
                function(half, x, y, a-half, b+half, 3)
                function(half, a, b, a+half, b+half, 4)
            #bottom right
            elif x >= a and y >= b:
                board[b-1][a-1], board[b][a-1], board[b-1][a] = "o", "o", "o"
                function(half, a-1, b-1, a-half, b-half, 1)
                function(half, a, b-1, a+half, b-half, 2)
                function(half, a-1, b, a-half, b+half, 3)
                function(half, x, y, a+half, b+half, 4)
                
    function(int(size/2), ex, ey, int(size/2), int(size/2), 1)
    for row in board: print("".join(row))
