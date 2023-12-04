#!/usr/bin/env python
# This file is executed when you run a package as the main program.
# The code in __main__.py is not run when the package is imported as a module

#When a package is executed using python -m package_name, Python looks for a 
#__main__.py file in the specified package. If found, it treats the package as a script, and the code in __main__.py is executed
"""Package entry point."""

from hel.cli import main

if __name__ == '__main__':  # pragma: no cover
    main()  # pylint: disable=no-value-for-parameter
