input_one = input()
input_two = input()
one = []
two = []
if len(input_one) < len(input_two):
    input_one, input_two = input_two, input_one
for i in input_one:
    one.append(int(i))
for i in input_two:
    two.append(int(i))
length = len(one)
add = [0] * (length + 1)
total = [0] * (length + 1)
one.reverse()
two.reverse()
count = 0
while count < length:
    temp = one[count] + two[count] + add[count]
    if temp >= 10:
        total[count] = temp % 10
        add[count+1] = (temp - temp % 10) / 10
    else:
        total[count] = temp
    count += 1
total[-1] = add[-1]
total.reverse()
final = []
for i in total:
    final.append(str(int(i)))
print(final)
if final[0] == "0":
    print("".join(final[1:]))
else:
    print("".join(final))
