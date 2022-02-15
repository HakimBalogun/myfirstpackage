from setuptools import setup, find_packages 

setup(
    name = 'myfirstpackage',
    version = '0.1',
    packages = find_packages(exclude = ['tests*']),
    license = 'MIT',
    description = 'EDSA example python package',
    long_description = open('README.md').read(),
    install_requires = ['numpy'],
    url = 'http://github.com/<HakimBalogun>/<package-name>',
    author = 'Hakim Balogun',
    author_email = 'hakim.obalogun@gmail.com' 
)
