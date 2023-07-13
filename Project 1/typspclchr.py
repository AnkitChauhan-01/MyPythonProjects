#This program prints special & numeric characters one at a time and the user have to type the same character as well as his will to continue typing.

file = open('specialchars.txt','r')

file2=file.read()
e=True
while(e):
    str = file2[random.randint(0,len(file2))]
    if((i==" ")or(i=="\n")):
        continue
    else:
        print("Type this: ",str)
        var= input()
        if(var==str):
            continue
        else:
            print("Wrong input!\nTry again or type 'NO' for exit.")
            var2= input()
            if(var2=="NO"):
                e=False
