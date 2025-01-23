from pathlib import Path

#These are the extensions for the Pentax camera.
#Change them if you want to use this script with a different raw file.
target_extensions = [".pef", ".xmp"]

folder_name = input("What would you like the folder to be called? This name will be used for RAW, OOC jpeg, and and your output folder: ")
raw_name = folder_name + "_raw"
folder_path = Path(raw_name)
folder_path.mkdir(exist_ok=True)

print(f"Folder '{folder_name}' has been created.")


for file in Path.cwd().iterdir():
    if file.is_file():
        ext = file.suffix.lower()
        if ext in target_extensions:
            dest = folder_path / file.name
            file.rename(dest)
            print(f"Moved: {file.name} ➔ {folder_name}/")
