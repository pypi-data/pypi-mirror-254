from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()

DOCS = """Color palette is a python library for working with 
various color formats such as RGB and HEX. 
This project is currently under development, but you can already use this library to work with colors. 
So far, color_palette supports only HEX and RGB, but other formats will be added in the future."""

setup(
    name='cpalette',
    version='1.0.5',
    author='chebupelka8',
    author_email='stpzamyatin@gmail.com',
    description=DOCS,
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/chebupelka8/CPalette',
    packages=find_packages(),
    install_requires=['pillow'],
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.7'
)
