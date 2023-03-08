import os
import shutil
from os import path
import zipfile
import pathlib

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u","f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = {}

for cir, lat in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(cir)]=lat
        TRANS[ord(cir.upper())]=lat.upper()

def normalise(text):
        return text.translate(TRANS)

SORTING_DICT = {'picture':['.jpg', '.bmp', '.jpg', '.png'],
                'video':['.avi', '.mp4', '.wmv', '.3gpp'],
                'documents':['.doc', '.docx', '.xls', '.xlsx' '.txt', '.pdf', '.pptx'],
                'music':['.mp3', '.wav', '.flac', '.aac', 'ogg', 'amr'],
                'archives':['.zip', '.rar', 'gz', 'tar'],
                'other': []}

def reed_dir(dir):
        file_cr = []
        for i in os.listdir(dir):
                file_cr.append(i) 
        print (file_cr)
        return file_cr
        

def translate(normalise):
        for cir, lat in zip(CYRILLIC_SYMBOLS, TRANSLATION):
                TRANS[ord(cir)]=lat
                TRANS[ord(cir.upper())]=lat.upper()
                last_name = normalise.translate(TRANS)        

        return last_name
translate("")

def rename(file_cr, root_dir):
        for i in file_cr:
                os.rename(os.path.join(root_dir, i), os.path.join(root_dir, normalise(i)))

if __name__ == "__main__":
        root_dir = r'f:\Dell\test_dir'
        file_list = reed_dir(root_dir)
        rename(file_list, root_dir)
        reed_dir(root_dir)



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
                        shutil.move(fr"f:\Dell\test_dir\{file}", fr"f:\Dell\test_dir\arhive")
                        shutil.unpack_archive(fr'f:\Dell\test_dir\arhive\{file}', fr'f:\Dell\test_dir\arhive')
        
                else:
                        try:
                                shutil.move(fr"f:\Dell\test_dir\{file}", fr"f:\Dell\\test_dir\unknown")
                        except FileNotFoundError:
                                continue
sort_dir("f:\Dell\\test_dir")






