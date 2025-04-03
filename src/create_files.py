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

    
def create_files():
    """runs create files to clean and create files in public"""

    public_path = "./public"
    static_path = "./static"

    if not os.path.exists(public_path):
        raise FileNotFoundError("Directory 'public' does not exist")
    if not os.path.exists(static_path):
        raise FileNotFoundError("Directory 'static' does not exist")
    print("Deleting public directory")
    clean_public(public_path)
    print("Copying static files to public")
    copy_files(static_path, public_path)
 
