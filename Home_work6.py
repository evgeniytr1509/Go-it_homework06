import os
import shutil
from os import path

def sort_dir(dirr):
        file_list = []
        for i in os.listdir(dirr):
                file_list.append(i) 

        print (file_list)
        
sort_dir("f:\Dell\\test_dir")

print ("*************")
def translate(normalise):
        CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
        TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u","f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
        TRANS = {}
        for cir, lat in zip(CYRILLIC_SYMBOLS, TRANSLATION):
                TRANS[ord(cir)]=lat
                TRANS[ord(cir.upper())]=lat.upper()
                last_name = normalise.translate(TRANS)        
                #os.rename('f:\\Dell\\test_dir\{first_name}', "f:\\Dell\\test_dir\\{last_name}")                
                
        print (f"name_latin - {last_name}")
        return last_name
translate("")

def file_list(dirr):
        test_lat = []
        for i in os.listdir(dirr):
                test_lat.append(translate(i))  
                
file_list("f:\Dell\\test_dir")


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
        
                if file.endswith('zip') == True:
                        shutil.move(fr"f:\Dell\test_dir\{file}", fr"f:\Dell\\arhive")
        
                # else:
                        #     shutil.move(fr"f:\Dell\test_dir\{file}", fr"f:\Dell\\unknown")
        

sort_dir("f:\Dell\\test_dir")






