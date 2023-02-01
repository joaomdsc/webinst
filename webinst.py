# webinst -- instantiate a web application skeleton

import os
import sys
from venv import EnvBuilder
from shutil import copytree
from subprocess import run, PIPE, STDOUT

def expanduser(path):
    r"""Expand ~ using HOME instead of Windows-specific stuff.

    The standard os.path.expanduser() replaces my ~ with
    C:\Users\joao.moreira.INV, but I have defined a different HOME
    variable that I want to use. 
    """
    if path.startswith('~'):
        # Remove '~/', not just '~', to avoid an absolute path, otherwise the
        # HOME segment will be ignored.
        return os.path.join(os.getenv('HOME'), path[2:])
    return path

def webinst(dst_path, app_name, rest=False):
    # app_path is the directory that will hold the app
    dst_path = expanduser(dst_path)
    print(f'dst_path={dst_path}')
    
    if not os.path.isdir(dst_path):
        os.makedirs(dst_path)
    app_path = os.path.join(dst_path, app_name)
    
    # Copy skeleton sub-tree and move into it
    src = 'skel_rest' if rest else 'skel'
    copytree(src, app_path)
    os.chdir(app_path)
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
    r = run([p, '-m', 'pip', 'install', 'flask-wtf'], stdout=PIPE, stderr=STDOUT)
    if rest:
        print('Installing the connexion[swagger-ui] module')
        r = run([p, '-m', 'pip', 'install', 'connexion[swagger-ui]'], stdout=PIPE, stderr=STDOUT)

    with open('requirements.txt', 'w', encoding='utf-8') as f:
        r = run([p, '-m', 'pip', 'freeze'], stdout=f, stderr=STDOUT)

if __name__ == '__main__':
    # Command line argument
    if len(sys.argv) < 3:
        print(f"""\
Usage: {sys.argv[0]} <dst_path> <app_name> [rest]

Create the app_name subdirectory inside dst_path. If dst_path does not exist,
the script will create it. If rest is set, generate a different app skeleton
that uses the connexion module to offer a swagger description of a REST API.\
""")
        exit(-1)
    rest = False
    if len(sys.argv) > 3:
        rest = sys.argv[3] == 'rest'
    webinst(sys.argv[1], sys.argv[2], rest=rest)
