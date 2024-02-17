from setuptools import setup, find_packages

setup(
    name='LeetifyPy',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'selenium',
    ],
    entry_points={
        'console_scripts': [
            'LeetifyPy-cli = LeetifyPy.cli:main',  # If you have a command-line interface
        ],
    },
    author='Phial',
    author_email='phialdial@example.com',
    description='A web scraping library using Selenium for Leetify to get player data.',
    long_description = '''
Leetify Web Scraping Library

The Leetify Web Scraping Library is a Python package designed to facilitate the extraction of player data from the popular gaming platform Leetify. Leveraging the power of Selenium, this library provides a seamless interface to retrieve essential information about players, including their names, win rates, and teammate details.

'''
,
    url='https://github.com/PhialsBasement/LeetifyPy',
    license='MIT',
classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
],

)
