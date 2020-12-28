total = int(input())
count = 0
names = {}
while count < total:
    name = input()
    names[name] = int(input())
    count += 1
for i in sorted(names.items(), key=lambda x: x[1], reverse=True):
    print(i[0] + " " + str(i[1]))
