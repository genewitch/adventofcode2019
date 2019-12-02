intar = []
clean = []
a = 0
with open('input3.txt') as f: # REPLACE "," WITH "\N"
    commands = list(f)
for string in commands:         #yeah i dunno python, sue me.
    clean.append(int(string))
    
intar = clean[:]                #this actually makes a copy by value of the list
                                # intar = clean just makes a reference copy; stupid.

#main
for j in range(0,100):        
    for k in range(0,100):
        intar = []          #erase program
        intar = clean[:]    #reset the program
        intar[1] = j
        intar[2] = k
        a = 0
        
        #run the program
        while (True):
            
            if intar[a] == 1: #add
                intar[intar[a+3]] = intar[intar[a+1]] + intar[intar[a+2]]
            if intar[a] == 2: #multiply opcode
                intar[intar[a+3]] = intar[intar[a+1]] * intar[intar[a+2]]
            if intar[a] == 99: #halt opcode
                break
            a += 4              #skip to next opcode
        
        #check if we got it
        if intar[0] == 19690720:
            print (100 * j + k) #print the thing the page wants
            break
    #is there a better way?
    if intar[0] == 19690720:
        break

print ('----------------------------------------------------')
print (intar)