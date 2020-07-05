import os


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error : Creating directory: ' + directory)
        
print('make_dir imported')

def chgFolder(directory):
    curr_dir = os.getcwd()
    next_dir = os.path.join(curr_dir, directory)
    os.chdir(next_dir)
    
base_dir = os.getcwd()
base_dir = os.path.join(base_dir, 'data')
chgFolder(base_dir)

def chgDir(directory):
    os.chdir(directory)