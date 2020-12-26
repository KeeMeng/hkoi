balance = int(input())
for i in range(int(input())): balance -= int(input())
if balance == 0:
    print("$250")
elif balance < 0:
    print("$" + str(( int( - balance / 250 ) + 1 ) * 250 ))
else:
    print("$0")
