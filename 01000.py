import re
repetitions = int(input())
count = 1
while count <= repetitions:
    input_string = str(input())
    string = re.findall("\"(.*)\" (.*) \"(.*)\"", input_string)[0]
    if len(string[0]) > 40:
        output = string[0]
    elif string:
        if string[1] == "Cut":
            output = string[0].replace(string[2], "")
        elif string[1] == "Append":
            output = string[0] + string[2]
        elif string[1].startswith("Insert"):
            index = int(re.findall("Insert (\d\d?)", string[1])[0]) - 1
            output = string[0][:index] + string[2] + string[0][index:]
        elif string[1].startswith("Replace"):
            replace = re.findall("Replace \"(.*)\"", string[1])[0]
            output = re.sub(replace, string[2], string[0], 1)
        else:
            output = string[0]
    print("Command #" + str(count) + ": \"" + output + "\"")
    count += 1


##import re
##repetitions = int(input())
##count = 1
##while count <= repetitions:
##    input_string = str(input())
##    string = re.findall("\"(.*)\" (.*) \"(.*)\"", input_string)[0]
##    if string:
##        if string[1] == "Cut":
##            output = string[0].replace(string[2], "")
##        elif string[1] == "Append":
##            output = string[0] + string[2]
##        elif string[1].startswith("Insert"):
##            index = int(re.findall("Insert (\d\d?)", string[1])[0]) - 1
##            output = string[0][:index] + string[2] + string[0][index:]
##        elif string[1].startswith("Replace"):
##            replace = re.findall("Replace \"(.*)\"", string[1])[0]
##            output = re.sub(replace, string[2], string[0], 1)
##        else:
##            output = string[0]
##    print("Command #" + str(count) + ": \"" + output + "\"")
##    count += 1


##import re
##
##repetitions = int(input("Repetitions: "))
##count = 1
##input_string = str(input("Input String: "))
##print(input_string)
##input_string = re.findall("\"(.*)\" (.*) \"(.*)\"",input_string)
##print(input_string)
##while count < repetitions:
##    output = ""
##    string = input_string[count]
##    if string[1] == "Cut":
##        output = string[0].replace(string[2],"")
##    elif string[1] == "Append":
##        output = string[0] + string[2]
##    elif string[1].startswith("Insert"):
##        index = int(re.findall("Insert (\d\d?)",string[1])[0]) - 1
##        output = string[0][:index] + string[2] + string[0][index:]
##    elif string[1].startswith("Replace"):
##        replace = re.findall("Replace \"(.*)\"",string[1])[0]
##        output = re.sub(replace,string[2],string[0],1)
##    else:
##        output = string[0]
##    print("Command #" + str(count+1) + ": \"" + output + "\"")
##    count += 1
