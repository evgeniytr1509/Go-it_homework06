import os
import shutil
from os import path


def sort_dir(dirr):
        file_list = []
        for i in os.listdir(dirr):
                file_list.append(i) 
        print (file_list)
        for first_name in file_list:
                print (f" name_cyrillic - {first_name}")   
        return first_name             
sort_dir("f:\Dell\\test_dir")

def sort_dir(d):
        test = []
        for i in os.listdir(d):
                test.append(i)
        print (test)
        os.mkdir("f:\Dell\\test_dir\picture")
        os.mkdir("f:\Dell\\test_dir\python")
        os.mkdir("f:\Dell\\test_dir\documets")
        os.mkdir("f:\Dell\\test_dir\\video")
        os.mkdir("f:\Dell\\test_dir\music")
        os.mkdir("f:\Dell\\test_dir\\arhive") 
        os.mkdir("f:\Dell\\test_dir\\unknown")    

        for file in test:
                if file.endswith('jpg') == True:
                        shutil.move(fr"f:\Dell\\test_dir\{file}", fr"f:\Dell\\test_dir\picture")

                if file.endswith('py') == True:
                        shutil.move(fr"f:\Dell\test_dir\{file}", fr"f:\Dell\\test_dir\python")
        
                if file.endswith('doc') == True or file.endswith('xlsx') == True:
                        shutil.move(fr"f:\Dell\test_dir\{file}", fr"f:\Dell\\test_dir\documets") 
                
                if file.endswith('avi') == True or file.endswith('mp4') == True or file.endswith('flv') == True:
                        shutil.move(fr"f:\Dell\test_dir\{file}", fr"f:\Dell\\test_dir\video")  
        
                if file.endswith('mp3') == True:
                        shutil.move(fr"f:\Dell\test_dir\{file}", fr"f:\Dell\\test_dir\music") 
        
                if file.endswith('zip') == True or file.endswith('gz') == True:
                        shutil.move(fr"f:\Dell\test_dir\{file}", fr"f:\Dell\\arhive")
                
                else:
                        shutil.move(fr"f:\Dell\test_dir\{file}", fr"f:\Dell\\unknown")



sort_dir("f:\Dell\\test_dir")






