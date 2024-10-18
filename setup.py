from setuptools import setup, find_packages

setup(
    name='hygraph_core',       # Name of your package
    version='0.1.0',                 # Version of your package
    description='A package for managing and analyzing HyGraph data',
    long_description=open('README.md').read(),  # Read the content of README.md
    long_description_content_type='text/markdown',
    author='Mouna',
    author_email='',
    url='https://github.com/yourusername/my_hygraph_package',  # URL to the project repository
    packages=find_packages(),        # Automatically find packages in the directory
    install_requires=[
        'pandas',
        'networkx',
        'numpy',
        # Add other dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',         # Specify required Python version
)