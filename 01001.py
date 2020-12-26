import re
while True:
    string = str(input())
    if "\endinput" in string:
        print("\endinput")
        break
    splitted = string.split("\par")
    join = ""
    for i in splitted:
        i = i.replace("\\\\", "\\")
        length = len(re.findall("(?<!\\\)\"", i))
        if length % 2 == 1:
            reverse = i[::-1]
            reverse = reverse.replace("\"\\", "\\\"")
            normal = re.sub("(?<!\\\)\"", "", reverse, 1)
            normal = normal.replace("\\\"", "\"\\")
            join += normal[::-1]
        else:
            join += i
        join += "\par"
    output = re.sub("(?<!\\\)\"", "!!", join)
    old = ""
    while output != old:
        old = output
        output = re.sub("!!", "``", output, 1)
        output = re.sub("!!", "''", output, 1)
    output = output[:-4]
    print(output)
    
