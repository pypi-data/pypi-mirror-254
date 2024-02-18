from setuptools import setup, find_packages

setup(
    name='LeetifyPy',
    version='0.4',
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

Features


 get_player_name(): Extract the player name associated with a given account link on Leetify. The library navigates through the website's structure, locating the relevant elements and delivering accurate player names.

 get_player_win_rate(): Retrieve the win rate percentage of a player by supplying their Leetify account link. The library navigates dynamically loading pages, ensuring accurate and up-to-date win rate information.

 get_player_teammates(): Collect a dictionary of a player's teammates and their respective Leetify account links. The library intelligently identifies and fetches this data, providing a comprehensive overview of a player's gaming network.
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
