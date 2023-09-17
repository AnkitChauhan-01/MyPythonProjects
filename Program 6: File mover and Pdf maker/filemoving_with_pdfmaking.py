import os
import shutil
import IMAGE_CONVERTOR

def move(sf,df,sfn):
    
    source_folder = sf
    destination_folder = df
    stoping_file_name= sfn

    #This code block will create destination folder if it doesn't exists.
    if os.path.exists(destination_folder):
        pass
    else:
        os.makedirs(destination_folder)

    files_in_folder = os.listdir(source_folder) #This will contain a list of sorted names (in increasing order) of files from the source_folder directory.
    
    for i in range(len(files_in_folder),0,-1): #This loop will run in reverse direction. & Since, there are already some files in source_folder, zero condition will never be met.
        new_string = source_folder+"\\"+files_in_folder[i-1]
        if(new_string==stoping_file_name):
            break
        else:
            shutil.move(new_string, destination_folder)

    print("All files moved successfully!")

source_folder = input("Enter full path specified source_folder name: ")
destination_folder = input("Enter full path specified destination_folder name: ")
stoping_file_name = input("Enter full path specified stoping_file_name name: ")
new_pdf_name= input("Enter the new pdf name (HINT: Related to destination folder name) : ")

#Making function call:
move(source_folder,destination_folder,stoping_file_name)
IMAGE_CONVERTOR.func1(destination_folder,new_pdf_name)
