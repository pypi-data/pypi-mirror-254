from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'ZenGuard API Client'
LONG_DESCRIPTION = 'ZenGuard API Client'

# Setting up
setup(
        name="zenguard", 
        version=VERSION,
        author="Sheshen",
        author_email="sheshen@duck.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['websocket-client', 'requests', 'python-socketio'],
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)