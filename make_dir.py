import os


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error : Creating directory: ' + directory)
        
print('make_dir imported')

base_dir = os.getcwd()

def chgFolder(directory):
    curr_dir = os.getcwd()
    next_dir = os.path.join(curr_dir, directory)
    os.chdir(next_dir)
    
def set_dir(directory):
    global base_dir
    base_dir = os.path.join(base_dir, directory)
    createFolder(base_dir)
    chgFolder(base_dir)
    
def chgDir(directory):
    os.chdir(directory)