k = int(input().split(" ")[1])
l = input().split(" ")
small = 32767
for i in l:
    if abs(int(i) - int(k)) < small:
        small = abs(int(i) - int(k))
        s = i
    if abs(int(i) - int(k)) == small and i > s:
        s = i
print(s)
