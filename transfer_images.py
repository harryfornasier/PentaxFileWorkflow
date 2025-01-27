from pathlib import Path
import shutil
import os

#These are the extensions for the Pentax camera.
#Change them if you want to use this script with a different raw file.
target_extensions = [".pef", ".xmp"]

def check_saved(directory):
    folders_without_saved = []

    for root, dirs, files in os.walk(directory):
        for name in dirs:
            if "_saved" not in name:
                folders_without_saved.append(name)

    return folders_without_saved if folders_without_saved else False

new_folders = check_saved("./DCIM")

if new_folders:
    for folder in new_folders:
        folder_name = input(f"What would you like the folder {folder} to be called? This name will be used for RAW, OOC jpeg, and and your output folder: ")
        root_path = Path(os.path.expanduser(f"~/Pictures/{folder_name}"))
        os.mkdir(root_path)

        folder_path = Path(f"{root_path}/{folder_name}_raw")
        folder_path.mkdir(exist_ok=True)

        print(f"Folder '{folder_name}' has been created.")

        for file in Path(f"./DCIM/{folder}").iterdir():
            if file.is_file():
                ext = file.suffix.lower()
                if ext in target_extensions:
                    dest = folder_path
                    shutil.copy2(file, dest)
                    print(f"Copied: {file.name} ➔ {folder_name}/")
                else:
                    dest = root_path
                    shutil.copy2(file, dest)
                    print(f"Copied: {file.name} ➔ {folder_name}/")

        shutil.move(f"./DCIM/{folder}", f"./DCIM/{folder}_saved")
else:
    print("There seem to be no new folders")
