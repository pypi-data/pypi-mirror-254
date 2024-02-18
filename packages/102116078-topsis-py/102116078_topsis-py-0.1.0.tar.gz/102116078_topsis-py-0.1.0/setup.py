from setuptools import setup, find_packages

with open('README.md', 'r') as file:
    description = file.read()

setup(
    name='102116078_topsis-py',
    version='0.1.0',
    author='Dhruv',
    author_email='dkikan_be21@thapar.edu',
    description='Implementation of Topsis in Python',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            '102116078_topsis=topsis_code.main_code:main',
        ],
    },
    long_description = description, 
    long_description_content_type = "text/markdown",
)
