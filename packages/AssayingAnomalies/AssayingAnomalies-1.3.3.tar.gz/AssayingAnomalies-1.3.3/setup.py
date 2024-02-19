from setuptools import setup, find_packages

# Read requirements.txt and store its contents in the 'requirements' variable
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='AssayingAnomalies',
    version='1.3.3',
    author='Joshua Lawson',
    author_email='jlaws13@simon.rochester.edu',
    description='This library is a Python implementation of the MATLAB Toolkit that accompanies Novy-Marx and Velikov '
                '(2023) and is to be used for empirical academic asset pricing research, particularly focused on '
                'studying anomalies in the cross-section of stock returns.',
    packages=find_packages(),
    package_data={
        'AssayingAnomalies': ['Gibbs/*', 'High-frequency effective spreads/*'],
    },
    install_requires=requirements,
    long_description='Package installed successfully. Please run \'setup_library\' to configure your settings and '
                     'begin using the toolkit'
)

