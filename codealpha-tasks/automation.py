import os, shutil

def organize_files(folder_path):
    for file in os.listdir(folder_path):
        name, ext = os.path.splitext(file)
        ext = ext[1:]  # remove dot from extension
        if ext == "":
            continue
        folder = os.path.join(folder_path, ext)
        if not os.path.exists(folder):
            os.makedirs(folder)
        shutil.move(os.path.join(folder_path, file), os.path.join(folder, file))

folder_path = input("Enter folder path: ")
organize_files(folder_path)
print("✅ Files organized by type!")