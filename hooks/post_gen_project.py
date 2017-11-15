#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def remove_directory(dirpath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, dirpath))

def rename(filepath, newname):
    os.rename(os.path.join(PROJECT_DIRECTORY, filepath), os.path.join(PROJECT_DIRECTORY, newname), )   

def move(dirpath, dst):
    shutil.move(os.path.join(PROJECT_DIRECTORY, dirpath), os.path.join(PROJECT_DIRECTORY, dst))



if __name__ == '__main__':

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE.rst')
    
    # Create the project management tools
    #os.system("cd docs && make html && cd..")
    #os.system("git init && git flow init && git commit -m 'initial commit' ")
