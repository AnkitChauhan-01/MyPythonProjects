#This program prints special & numeric characters one at a time and the user have to type the same character as well as his will to continue typing.

file = open('specialchars.txt','r')

file2=file.read()
for i in file2:
    if((i==" ")or(i=="\n")):
        continue
    else:
        print(i)
    while(True):
        e = input("Type here: ")
        if(e==i):
            break
        else:
            print("Wrong input!")
            print("Enter again")