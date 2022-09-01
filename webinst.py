# webinst -- instantiate a web application skeleton

import os
import sys
import subprocess
from venv import EnvBuilder

def webinst(app_name):
    # Create sub-directory and move into it
    try:
        os.mkdir(app_name)
    except FileExistsError as e:
        print(f'Directory "{app_name}" already exists', file=sys.stderr)
        exit(-1)
    os.chdir(app_name)
    print(f'Current directory is "{os.getcwd()}"')

    # Run pip freeze outside venv
    

    # Create virtual environment
    env = EnvBuilder(with_pip=True)
    env.create('venv')
    print(f'Created virtual environment')
    
if __name__ == '__main__':
    # Command line argument
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <app_name>')
        exit(-1)
    webinst(sys.argv[1])
