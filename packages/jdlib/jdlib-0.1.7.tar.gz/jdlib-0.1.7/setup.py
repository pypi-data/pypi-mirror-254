from setuptools import setup, find_packages

setup(
    name='jdlib',
    version='0.1.7',
    author='Janus Digital LLC',
    author_email='justice@janusdigital.io',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'jdcli=jdlib.cli:main',
        ],
    }
)
