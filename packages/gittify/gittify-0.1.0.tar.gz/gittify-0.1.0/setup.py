from setuptools import setup, find_packages

setup(
    name='gittify',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'beautifish',
        'pywin32',
        'ctypes'
    ],
)