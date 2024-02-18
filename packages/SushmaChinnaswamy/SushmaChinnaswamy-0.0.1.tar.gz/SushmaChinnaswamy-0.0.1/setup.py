from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 1 - Planning',
    'Environment :: MacOS X',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.0'
]

setup(
    name='SushmaChinnaswamy',
    version='0.0.1',
    description='This is a very simple calculator',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Sushma Chinnaswamy',
    author_email='schinn13@asu.edu',
    license='MIT',
    classifiers=classifiers,
    keywords='',
    packages=find_packages(),
    install_requires=['']
)
