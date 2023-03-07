import os
import shutil
from os import path

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u","f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = {}

SORTING_DICT = {'picture':['.jpg', '.bmp', '.jpg', '.png'],
                'video':['.avi', '.mp4', '.wmv', '.3gpp'],
                'documents':['.doc', '.docx', '.xls', '.xlsx' '.txt', '.pdf', '.pptx'],
                'music':['.mp3', '.wav', '.flac', '.aac', 'ogg', 'amr'],
                'archives':['.zip', '.rar', 'gz', 'tar'],
                'other': []}

def reed_dir(dirr):
        file_cr = []
        for i in os.listdir(dirr):
                file_cr.append(i) 
        print (file_cr)
        # for first_name in file_list:
        #         print (first_name)
reed_dir("f:\Dell\\test_dir")

def translate(normalise):
        for cir, lat in zip(CYRILLIC_SYMBOLS, TRANSLATION):
                TRANS[ord(cir)]=lat
                TRANS[ord(cir.upper())]=lat.upper()
                last_name = normalise.translate(TRANS)        
                                        
        #print (f"name_latin - {last_name}")
        return last_name
translate("")

def file_list(dirr):
        file_lt = []
        for i in os.listdir(dirr):
                file_lt.append(translate(i))  
        print (file_lt)        
file_list("f:\Dell\\test_dir")

def rename(file_cr, file_lt):
        list_lt = []
        for i in os.listdir(file_cr):
            os.rename('f:\\Dell\\test_dir\{file_cr}', "f:\\Dell\\test_dir\\{file_lt}")
        print (list_lt)
rename(file_cr)


# def sort_dir(d):
#         test = []
#         for i in os.listdir(d):
#                 test.append(i)
#         print (test)
#         os.mkdir("f:\Dell\\test_dir\picture")
#         os.mkdir("f:\Dell\\test_dir\python")
#         os.mkdir("f:\Dell\\test_dir\documets")
#         os.mkdir("f:\Dell\\test_dir\\video")
#         os.mkdir("f:\Dell\\test_dir\music")
#         os.mkdir("f:\Dell\\test_dir\\arhive") 
#         os.mkdir("f:\Dell\\test_dir\\unknown")    

#         for file in test:
#                 if file.endswith('jpg') == True:
#                         shutil.move(fr"f:\Dell\\test_dir\{file}", fr"f:\Dell\\test_dir\picture")

#                 if file.endswith('py') == True:
#                         shutil.move(fr"f:\Dell\test_dir\{file}", fr"f:\Dell\\test_dir\python")
        
#                 if file.endswith('doc') == True or file.endswith('xlsx') == True:
#                         shutil.move(fr"f:\Dell\test_dir\{file}", fr"f:\Dell\\test_dir\documets") 
                
#                 if file.endswith('avi') == True or file.endswith('mp4') == True or file.endswith('flv') == True:
#                         shutil.move(fr"f:\Dell\test_dir\{file}", fr"f:\Dell\\test_dir\video")  
        
#                 if file.endswith('mp3') == True:
#                         shutil.move(fr"f:\Dell\test_dir\{file}", fr"f:\Dell\\test_dir\music") 
        
#                 if file.endswith('zip') == True:
#                         shutil.move(fr"f:\Dell\test_dir\{file}", fr"f:\Dell\\arhive")
        
#                 # else:
#                         #     shutil.move(fr"f:\Dell\test_dir\{file}", fr"f:\Dell\\unknown")
        

# sort_dir("f:\Dell\\test_dir")






