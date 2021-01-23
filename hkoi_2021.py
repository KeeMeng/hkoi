inps = input()
inp = inps.split(" ")
n = int(inp[0])
h = int(inp[1])
height = input()
heights = height.split(" ")
grid = []
for i in heights:
    temp = []
    c = 0
    while c <= h:
        temp.append(".")
        c = c + 1
    count = 0
    while count < int(i):
        temp[count] = "X"
        count = count + 1
    grid.append(temp)

length = int(input())
flights = input()
count = 0
flight = []
ever = 1
while count < len(flights):
    flight.append(flights[count])
    if flights[count] == "D":
        ever = 0
    count = count + 1

if ever == 1:
    print("FOREVER")

if ever == 0:
    x = 0
    y = h
    finish = 0
    while True:
        for f in flight:
            if finish == 0:
                if f == "N":
                    x = x + 1
                    if x == n:
                        x = 0
                    x = x - 1
                    index = x + 1
                    pos = grid[index][y]
                    if pos != "X":
                        x = x + 1
                    if pos == "X":
                        output = x + 1
                        print(f"SIDE\n{output}")
                        finish = 1

                if f == "D":
                    index = y - 1
                    pos = grid[x][index]
                    if pos != "X":
                        y = y - 1
                    if pos == "X":
                        output = x
                        print(f"TOP\n{output}")
                        finish = 1
        if finish == 1:
            break
