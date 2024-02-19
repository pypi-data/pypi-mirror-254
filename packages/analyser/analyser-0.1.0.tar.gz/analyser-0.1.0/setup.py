from setuptools import find_packages, setup

setup(
    name='analyser',
    version='0.1.0',
    author='Cale van der Westhuizen',
    author_email='cale@tks.co.za',
    packages=find_packages(where='analyser'),
    package_dir={'': 'analyser'},
    install_requires=[
        'numpy',
        'requests',
        'requests_mock',
    ],
    description='An analytical library for signal data analysis',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/calevdw/Analyser',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
