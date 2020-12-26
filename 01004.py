import re
alphabets = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
indices = input().split(" ")
m = re.findall("[A-Za-z0-9 ]+?\s+?\d+", input())
for i in m:
    string = re.sub("\s+", " ", i)
    shift = 27 - int(re.findall("\d+", string)[0]) % 27
    message = list(re.findall("[A-Za-z ]+", string)[0].strip())
    chars = [None] * 27
    count = 0
    output = ''
    while count < 27:
        chars[int(indices[count])] = alphabets[count]
        count += 1
    shifted = chars[shift:] + chars[:shift]
    for i in message:
        output += shifted[chars.index(i)]
    print("[" + output + "]")
