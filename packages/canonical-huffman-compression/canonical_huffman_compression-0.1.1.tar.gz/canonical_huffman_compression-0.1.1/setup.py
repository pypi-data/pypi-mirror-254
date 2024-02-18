from setuptools import setup, find_packages
# python setup.py sdist bdist_wheel
#  python -m twine upload dist/*
#  python -m twine upload --skip-existing dist/*
setup(
    name='canonical_huffman_compression',
    version='0.1.1',
    description='A package for canonical Huffman compression',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/craigwatkins/Huffman-Compression",
    author='Craig Watkins',
    author_email='craigwatkinsdev@gmail.com',
    packages=find_packages(),
    install_requires=[
        #
    ],
)