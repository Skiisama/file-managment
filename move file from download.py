import os
import shutil



#moves file from others to download
src_dir = r"C:\Users\USER\Desktop\Downloads\Others"
dst_dir = r"C:\Users\USER\Downloads"
movefilepls = False
if movefilepls:
    files = os.listdir(src_dir)
    for file in files:
        src_file = os.path.join(src_dir, file)
        dst_file = os.path.join(dst_dir, file)
        shutil.move(src_file, dst_file)



# Define the directory to scan
#C:\Users\USER\Downloads
#C:\Users\USER\Desktop\Downloads\Others
GOD = r"C:\Users\USER\Downloads"

# Define the directories to move files to based on their file type
dest_sound = r"C:\Users\USER\Downloads\Sound"
dest_vid = r"C:\Users\USER\Downloads\Videos"
dest_doc = r"C:\Users\USER\Downloads\Doc"
dest_zip = r"C:\Users\USER\Downloads\Zip"
dest_pic = r"C:\Users\USER\Downloads\Photo"
dest_other = r"C:\Users\USER\Downloads\Others"
dest_program = r"C:\Users\USER\Downloads\Program"
dest_folder = r"C:\Users\USER\Downloads\Folder"
dest_jar = r"C:\Users\USER\Downloads\Mods" 

ignore_name = "doc" , "videos","sound","zip","photo","others","program", "folder" , "mods"


# Define a function to move files to their destination directory
def move(dest, entry, name):
    if name in ignore_name:
        print(f"Ignoring file: {name}")
        shutil.move(dest, dest)
    else:
        shutil.move(entry.path, dest)

# sort files in GOD in to types
with os.scandir(GOD) as entries:
    for entry in entries:
        name = entry.name.lower()
        dest = GOD

        if name.endswith('.wav') or name.endswith('.mp3') or name.endswith('.m4a'):
            dest = dest_sound
            move(dest, entry, name)
        elif name.endswith('.mp4') or name.endswith('.mov'):
            dest = dest_vid
            move(dest, entry, name)
        elif name.endswith('.pdf') or name.endswith('.doc')or name.endswith('.docx'):
            dest = dest_doc
            move(dest, entry, name)
        elif name.endswith('.zip') or name.endswith('.rar'):
            dest = dest_zip
            move(dest, entry, name)
        elif name.endswith('.png') or name.endswith('.jpg') or name.endswith('jpeg') or name.endswith('gif') or name.endswith('.webp') \
             or name.endswith('.tga') or name.endswith('.heic') or name.endswith('.jfif') or name.endswith('.psd'):
            dest = dest_pic
            move(dest, entry, name)
        elif name.endswith('.exe'):
            dest = dest_program
            move(dest, entry, name)
        elif name.endswith('.jar'):
            dest = dest_jar
            move(dest, entry, name)
        elif entry.is_dir():
            dest = dest_folder
            move(dest, entry, name)
        else:
            dest = dest_other
            move(dest, entry, name)
