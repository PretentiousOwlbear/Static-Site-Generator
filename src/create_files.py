import os
import shutil

def clean_public(public_path):
    """Cleans out the public directory"""
    
    shutil.rmtree(public_path)
    os.mkdir(public_path)
    

def copy_files(file_path, file_dest):
    """copies files from static into public"""

    static_dirs = os.listdir(f"{file_path}")
    for dirs in static_dirs:
        path = os.path.join(file_path, dirs)
        dest = os.path.join(file_dest, dirs)

        if os.path.isfile(path):
            shutil.copy(f"{path}",f"{dest}")
        else:
            os.mkdir(f"{dest}")
            copy_files(f"{path}", f"{dest}")

    
def create_files(public_path, static_path):
    """runs create files to clean and create files in public"""

    
    if os.path.exists(public_path):
        print(f"Deleting {public_path} directory")
        shutil.rmtree(public_path)

    if not os.path.exists(public_path):
        os.mkdir(public_path)
        
    if not os.path.exists(static_path):
        raise FileNotFoundError("Directory 'static' does not exist")
    
    clean_public(public_path)
    print(f"Copying static files to {public_path}")
    copy_files(static_path, public_path)
 
