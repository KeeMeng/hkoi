string = input().split(" ")
num = int(string[0])
den = int(string[1])
result = num/den
if len(str(result)) > 17:
    count = 1
    while True:
        print(str(result * (10 ** count) - result))
        if len(str(result * (10 ** count) - result)) < 17:
            print(count)
            break
        count += 1
    s = str(result).split(".")
    print(s[0] + ".[" + s[1][:count] + "]")
else:
    print(result)
