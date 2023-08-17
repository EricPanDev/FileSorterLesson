# Module Imports
import os
import sys

# Code to get folder location
try:
    # Set Folder to Organize to the first sys.argv param
    folder_to_organize = sys.argv[1]
except IndexError:
    # No params specified, alert and exit
    print("Please specify a folder to organize!")
    exit()

def files_in_folder(folders:dict):
    for item in os.listdir(os.curdir):
        if not item in folders:
            yield item

def clean_folder(working_dir: str) -> bool:
    # try:
        os.chdir(working_dir)

        images = ["png", "jpeg", "jpg", "webp", "apng", "gif", "webp"]
        documents = ["pdf", "docx"]
        audio = ["mp3", "wav", "ogg"]
        archives = ["zip", "7z", "tar.gz", "tar"]

        folders = {"Media": images, "Documents": documents, "Audio": audio, "Archives": archives, "Folders": "folders", "Miscellanious": "misc"}

        for folder in folders:
            if not os.path.exists(folder):
                print("Creating a", folder, "folder")
                os.makedirs(folder)

        for item in files_in_folder(folder):
            if (not os.path.isfile(item)) and (not item in folders):
                os.rename(item, f"Folders/{item}")
                item = True
            elif item in folders:
                item = True
            else:
                for folder_name, mimetypes in folders.items():
                    for mimetype in mimetypes:
                        if not isinstance(item, str):
                            break
                        if item.endswith(f".{mimetype}"):
                            print(f"{folder_name}/{item}")
                            os.rename(item, f"{folder_name}/{item}")
                            item = True
                            break
            if item != True:
                os.rename(item, f"Miscellanious/{item}")

        return True
    # except:
    #     return False


if os.path.exists(folder_to_organize) == True: # Exists
    print(f"Organizing", folder_to_organize + "...")
    cleaned = clean_folder(folder_to_organize)

    if cleaned == True:
        print(f"Folder", folder_to_organize, "finished organizing!")
    else:
        print("Something went wrong while organizing your folder :(")

else: # NonExistant
    print("The folder you specified does not exist!")
    exit()
