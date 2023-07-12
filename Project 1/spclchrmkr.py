#This program prints special & numeric characters and of a text document.

file = open('rawtext.txt','r')
file2 = file.read()

for i in file2:
    
    if(i.isalpha()):
        continue
    elif(i==" " or i=="\n"):
        continue
    else:
        print(i,end=" ")