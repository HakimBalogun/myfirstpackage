from setuptools import setup, find_packages 

setup(
    name = 'myfirstpackage',
    version = '0.1',
    packages = find_packages(exclude = ['tests*']),
    license = 'MIT',
    description = 'EDSA example python package',
    long_description = open('README.md').read(),
    install_requires = ['numpy'],
    url = 'https://github.com/HakimBalogun/myfirstpackage.git',
    author = 'Hakim Balogun',
    author_email = 'addhak@gmail.com' 
)
