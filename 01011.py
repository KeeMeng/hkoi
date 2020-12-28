string = input()
old = ""
while old != string: old, string = string, string.replace("()", "").replace("[]", "").replace("{}", "")
print("Yes" if string == "" else "No")
