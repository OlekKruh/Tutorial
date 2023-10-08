from setuptools import setup, find_packages

setup(
    name='clean-folder',
    version='v2.1',
    description='Module for data tidying',
    author='A_Kross',
    author_email='ksalexks@gmail.com',
    packages=find_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']},
)
