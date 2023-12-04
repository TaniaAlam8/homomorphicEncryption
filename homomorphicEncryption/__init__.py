# The __init__.py file is a special file that Python recognizes as the package's initialization file. 
# used to mark a directory as a python package which contains related modules

# geometry is a package while shapes and operations are subpackages
# geometry/
#├── __init__.py
#├── shapes/
#│   ├── __init__.py
#│   ├── circle.py
#│   └── square.py
#└── operations/
#    ├── __init__.py
#    ├── area.py
#    └── perimeter.py

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version('homomorphicEncryption')
except PackageNotFoundError:
    __version__ = '(local)'

del PackageNotFoundError
del version
