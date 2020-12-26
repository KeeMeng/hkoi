size = 2 ** int(input())
half = int(size / 2)
empty = input().split(" ")
ex = int(empty[0])-1
ey = int(empty[1])-1
board = [["0"] * size for i in range(size)]
board[ex][ey] = "*"



for x in board: print("".join(x))
