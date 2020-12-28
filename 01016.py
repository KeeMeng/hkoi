length = int(input())
array = input().split(" ")
if length == len(array) and 1 <= length <= 100000:
    chain = []
    for i in array:
        chain.append(int(i))
    for i in array:
        chain.append(int(i))
    start = 0
    end = 0
    top = -1000000000
    while start < length * 2:
        while end <= length * 2 and end - start < length:
            temp = sum(chain[start:end])
            if temp > top:
                top = temp
            end += 1
        start += 1
        end = start
    print(top)
