from setuptools import setup, find_packages

VERSION = '0.1.0' 
DESCRIPTION = 'Client package for python logging with beaver logs'
LONG_DESCRIPTION = 'A fully programmatic logging system'

# Setting up
setup(
        name="beaver-logs", 
        version=VERSION,
        author="Will Priebe",
        author_email="wpriebe16124@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['socketio'],
        keywords=['python', 'logging'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)