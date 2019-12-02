total = 0
with open('moduleinput.txt') as f:
    textlist = list(f)
for line in textlist:
    modulerunning = (int(line)//3)-2 #has just the modules fuel for now
    moduletotal = modulerunning      # just the module fuel for now   
    temp= 0
    while (True):
        modulerunning =(int(modulerunning)//3)-2 # run the same opration as before
        if modulerunning <=0:                    # until we get 0 or negative
            break
        moduletotal += modulerunning             #tally
    
    total += moduletotal                         #total fuel count

print (total)