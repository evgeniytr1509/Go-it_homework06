import os
import shutil
from os import path

def sort_dir(d):
    test = []
    
    for i in os.listdir(d):
        test.append(i)
    print (test)

    for file in test:
        if file.endswith('jpg') == True:
            print ("file - Picture")
            source_path = ".jpg"
            if path.exists(source_path):
                destination_path = "f:\\Dell\test_dir\picture" # место перемещения файла
                new_location = shutil.move(source_path, destination_path) # перемещения файла

        if file.endswith('py') == True:
            print ("file - Python")
        if file.endswith('doc') == True:
            print ("file - Word") 
        if file.endswith('xlsx') == True:
            print ("file - Excel")
        if file.endswith('avi') == True:
            print ("file - Video")  
        else:
            print ("unknown file")
        
sort_dir("test_dir")


# str1 = "Hello world!"
# print (str1.endswith('ld!') == True)



