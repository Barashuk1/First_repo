import sys
import os
import shutil

IMAGES = ('JPEG', 'PNG', 'JPG', 'SVG')
VIDEO = ('AVI', 'MP4', 'MOV', 'MKV')
DOCUMENTS = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
AUDIO = ('MP3', 'OGG', 'WAV', 'AMR')
ARCHIVES = ('ZIP', 'GZ', 'TAR')

def normalize(file_name):
    TRANS = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g',
        'д': 'd', 'е': 'e', 'є': 'ie', 'ж': 'zh', 'з': 'z',
        'и': 'y', 'і': 'i', 'ї': 'i', 'й': 'i', 'к': 'k',
        'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
        'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f',
        'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
        'ь': '', 'ю': 'iu', 'я': 'ia'
    }

    new_file_name = ""
    for ch in file_name:
        if ch.lower() in TRANS:
            if ch.isupper():
                new_file_name += TRANS[ch.lower()].capitalize()
            else:
                new_file_name += TRANS[ch.lower()]
        elif ch.isalnum():
            new_file_name += ch
        else:
            new_file_name += '_'

    return new_file_name

def create_folder(folder_path):
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Folder {folder_path} was created")
        else:
            print(f"Folder {folder_path} exists")
    except OSError:
        print("OSError")

def remove_empty_folders(folder_path):
    if not os.path.exists(folder_path):
        print("Folder doesn`t exists")
        return
    
    for root, dirs, _ in os.walk(folder_path, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            
            if not os.listdir(dir_path):
                os.rmdir(dir_path)

def move_file(file_path, folder_path):
    if not os.path.exists(file_path):
        print("File doesn`t exists")
        return

    file_name = os.path.basename(file_path)
    destination_path = os.path.join(folder_path, file_name)

    if not os.path.exists(destination_path):
        shutil.move(file_path, destination_path)
        
def sort(folder_path, dict):
    contents = os.listdir(folder_path)
    
    for item in contents:
        if os.path.isfile(folder_path + "/" + str(item)):
            first_part = ".".join(str(item).split(".")[:-1])
            format = str(str(item).split(".")[-1]).upper()
            if format in IMAGES:
                shutil.move(folder_path + "/" + str(item), folder_path + "/" + normalize(first_part) + '.' + format.lower())
                item = normalize(first_part) + '.' + format.lower()
                move_file(folder_path + '/' + item, folder_path + '/' + "images")
          
            elif format in VIDEO:
                shutil.move(folder_path + "/" + str(item), folder_path + "/" + normalize(first_part) + '.' + format.lower())
                item = normalize(first_part) + '.' + format.lower()
                move_file(folder_path + '/' + item, folder_path + '/' + "video")
           
            elif format in AUDIO:
                shutil.move(folder_path + "/" + str(item), folder_path + "/" + normalize(first_part) + '.' + format.lower())
                item = normalize(first_part) + '.' + format.lower()
                move_file(folder_path + '/' + item, folder_path + '/' + "audio")
          
            elif format in DOCUMENTS:
                shutil.move(folder_path + "/" + str(item), folder_path + "/" + normalize(first_part) + '.' + format.lower())
                item = normalize(first_part) + '.' + format.lower()
                move_file(folder_path + '/' + item, folder_path + '/' + "documents")
            
            elif format in ARCHIVES:
                shutil.move(folder_path + "/" + str(item), folder_path + "/" + normalize(first_part) + '.' + format.lower())
                item = normalize(first_part) + '.' + format.lower()
                move_file(folder_path + '/' + item, folder_path + '/' + "archives")
               
            else:
                shutil.move(folder_path + "/" + str(item), folder_path + "/" + normalize(first_part) + '.' + format.lower())
                item = normalize(first_part) + '.' + format.lower()
                move_file(folder_path + '/' + item, folder_path + '/' + "unknown")
        else:
            sort(folder_path + "/" + str(item), dict)
    

def main():
    if len(sys.argv) == 2:
        folder_path = sys.argv[1]
        if os.path.isdir(folder_path):
            
            create_folder(folder_path + 'images')
            create_folder(folder_path + 'video')
            create_folder(folder_path + 'audio')
            create_folder(folder_path + 'documents')
            create_folder(folder_path + 'archives')
            create_folder(folder_path + 'unknown')
            
            sort(folder_path, dict)

            remove_empty_folders(folder_path)
        else:
            print("Enter folder")
    else: 
        print("Enter folder")


if __name__ == "__main__":
    main()
    