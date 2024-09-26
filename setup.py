from setuptools import setup, find_packages

setup(
    name='TermGPT',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'gpt=TermGPT.main:main_function',
        ],
    },
)