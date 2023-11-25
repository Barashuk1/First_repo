from setuptools import setup

setup(
    name='clean_folder',
    version='1.0',
    description='Code to sort your files',
    url='https://github.com/Barashuk1/First_repo',
    author='Barabash Ivan',
    author_email='top.player.vertuha228@gmail.com',
    license='MIT',
    packages=['clean_folder'],
    install_requires=[],
    long_description="Some long desctiption",
    long_description_content_type="text/x-rst",
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:main'
        ]
    },
)