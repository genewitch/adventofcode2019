intar = []
a = 0
with open('input3.txt') as f:
    commands = list(f)
for string in commands:
    intar.append(int(string))
print (intar)
while (True):
    print (intar[a])
    if intar[a] == 1:
        intar[intar[a+3]] = intar[intar[a+1]] + intar[intar[a+2]]
    if intar[a] == 2:
        intar[intar[a+3]] = intar[intar[a+1]] * intar[intar[a+2]]
    if intar[a] == 99:
        break
    a += 4
     
print ('----------------------------------------------------')
print (intar)