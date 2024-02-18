from setuptools import setup, find_packages

setup(
    name='CS270Boi',
    version='1.2.2',
    author='Jake Cahoon',
    author_email='jacobbcahoon@gmail.com',
    packages=find_packages(),
    url='http://pypi.python.org/pypi/CS270Boi/',
    license='LICENSE.txt',
    description='An awesome package for discussions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        "ipywidgets",
        "IPython",
    ],
)
