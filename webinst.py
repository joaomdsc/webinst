# webinst -- instantiate a web application skeleton

import os
import sys
from venv import EnvBuilder
from shutil import copytree
from subprocess import run, PIPE, STDOUT

def webinst(app_name):
    # Copy skeleton sub-tree and move into it
    copytree('skel', app_name)
    os.chdir(app_name)
    print(f'Current directory is "{os.getcwd()}"')

    # Create virtual environment
    env = EnvBuilder(with_pip=True)
    env.create('venv')
    print(f'Created virtual environment')

    # Python executable inside the venv
    p = os.path.join(os.getcwd(), 'venv', 'Scripts', 'python.exe')

    # Run python code inside the venv, as determined by the python exe
    print(f'Running pip install/freeze inside venv')
    r = run([p, '-m', 'pip', 'install', 'flask'], stdout=PIPE, stderr=STDOUT)
    r = run([p, '-m', 'pip', 'install', 'python-dotenv'], stdout=PIPE, stderr=STDOUT)

if __name__ == '__main__':
    # Command line argument
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <app_name>')
        exit(-1)
    webinst(sys.argv[1])
