l = [None] * int(input())
while True:
    packet = input()[3:]
    serial = int(packet[0:2])
    check = int(packet[2:6])
    data  = packet[6:]
    if sum(map(ord, data)) == check: l[serial-1] = data 
    if None not in l: break
print("".join(l))
