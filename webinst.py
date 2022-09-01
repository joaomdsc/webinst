# webinst -- instantiate a web application skeleton

import os
import sys
from venv import EnvBuilder
from subprocess import run, PIPE, STDOUT

def webinst(app_name):
    # Run pip freeze outside venv
    r = run(['pip', 'freeze'], stdout=PIPE, stderr=STDOUT)
    with open('venv_outside.txt', 'w', encoding='utf-8') as f:
        f.write(r.stdout.decode())
    
    # Create sub-directory and move into it
    try:
        os.mkdir(app_name)
    except FileExistsError as e:
        print(f'Directory "{app_name}" already exists', file=sys.stderr)
        exit(-1)
    os.chdir(app_name)
    print(f'Current directory is "{os.getcwd()}"')

    # Create virtual environment
    env = EnvBuilder(with_pip=True)
    env.create('venv')
    print(f'Created virtual environment')

    # Python executable inside the venv
    p = os.path.join(os.getcwd(), 'venv')
    p = os.path.join(p, 'Scripts')
    p = os.path.join(p, 'python.exe')

    # Run python code inside the venv, as determined by the python exe
    print(f'Running pip install/freeze inside venv')
    r = run([p, '-m', 'pip', 'install', 'simplejson'], stdout=PIPE, stderr=STDOUT)
    r = run([p, '-m', 'pip', 'freeze'], stdout=PIPE, stderr=STDOUT)
    with open('venv_inside.txt', 'w', encoding='utf-8') as f:
        f.write(r.stdout.decode())

if __name__ == '__main__':
    # Command line argument
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <app_name>')
        exit(-1)
    webinst(sys.argv[1])
