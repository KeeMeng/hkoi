inp = input().split(" ")
r = int(inp[0])
c = int(inp[1])
n = int(inp[2])
m = r + c - 1
count = 0
obstacles = []
output = []
while count < n:
    xy = input().split(" ")
    obstacles.append([int(xy[0]),int(xy[1])])
    count += 1

board = []
count = 0
while count < r:
    board.append(["."] * c)
    count += 1

for o in obstacles:
    board[o[0]-1][o[1]-1] = "O"

board[0][0] = "A"
# [print(i) for i in board]

# output.append(pos[-2])

def path(boards):
    pos = [[0,0]]
    no = []
    while True:
        coords = pos[-1]

        b = False
        #Vertical
        if coords[0] != r-1 and not b:
            if boards[coords[0]+1][coords[1]] != "O" and [coords[0]+1, coords[1]] not in no:
                # print("v")
                # print([coords[0]+1, coords[1]])
                pos.append([coords[0]+1, coords[1]])
                b = True
        
        #Horizontal
        if coords[1] != c-1 and not b:
            if boards[coords[0]][coords[1]+1] != "O" and [coords[0], coords[1]+1] not in no:
                # print("h")
                # print([coords[0], coords[1]+1])
                pos.append([coords[0], coords[1]+1])
                b = True

        if not b:
            # print("pop")
            pos.pop()
            no.append([coords[0], coords[1]])
        
        if len(pos) <= 0:
            return None
            break
        
        if pos[-1] == [r-1, c-1]:
            return pos
            break


re = path(board)
if re == None:
    print(0)
    
else:
    one = False
    count = 1
    while count < len(re) - 1:
        index = - count - 1
        arg = board[:]
        arg[re[index][0]][re[index][1]] = "O"

        value = path(arg)
        if value == None:
            one = True
            break
        count += 1

    if one:
        print(1)
        print(f"{re[index][0]+1} {re[index][1]+1}")
    else:
        print(2)
        print(f"{re[index][0]+1} {re[index][1]+1}")
        print(f"{value[index][0]+1} {value[index][1]+1}")


# [print(i) for i in board]

# print(output)


##print(len(output))
##for i in output:
##    print(f"{i[0]+1} {i[1]+1}")
