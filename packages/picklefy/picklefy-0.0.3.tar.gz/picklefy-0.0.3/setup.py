from pathlib import Path
from setuptools import setup, find_packages
from picklefy import __version__

DESCRIPTION = 'Um facilitador para trabalhar com pickle files'

setup(
    name="picklefy",
    version=__version__,
    author="Henrique Spencer Albuquerque",
    author_email="<henriquespencer11@gmail.com>",
    description=DESCRIPTION,
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    #install_requires=['pickle'],
    keywords=['python', 'pickle', 'serialize', 'deserializar', 'arquivos', 'facilitador', 'picklefy', 'picklefy'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Utilities",
    ],
    python_requires='>=3.6',
)