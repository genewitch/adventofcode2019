total = 0
with open('input1.txt') as f:
    textlist = list(f)
for line in textlist:
    temp = 0
    temp =(int(line)//3)-2
    total += temp

print (total)