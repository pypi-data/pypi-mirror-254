from setuptools import setup, find_packages


VERSION = '0.0.6'
DESCRIPTION = 'pyWrites to files package!'
LONG_DESCRIPTION = 'A simple package that lets you write faster to files! Watch the whole documentation at https://github.com/timoo4devv/pyWrite'

# Setting up
setup(
    name="pyWrites",
    version=VERSION,
    author="Beere",
    author_email="<timoschneiderr@outlook.de>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['cryptography'],
    keywords=['python', 'write', 'File', 'pyWrites', 'read', 'delete'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)