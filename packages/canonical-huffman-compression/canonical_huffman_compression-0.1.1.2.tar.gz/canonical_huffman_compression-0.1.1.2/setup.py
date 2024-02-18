from setuptools import setup, find_packages
# python setup.py sdist bdist_wheel
#  python -m twine upload dist/*
#  python -m twine upload --skip-existing dist/*
setup(
    name='canonical_huffman_compression',
    version='0.1.1.2',
    description='A package for canonical Huffman compression',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/craigwatkins/Huffman-Compression",
    author='Craig Watkins',
    author_email='craigwatkinsdev@gmail.com',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='huffman compression canonical',
    license='MIT',
    python_requires='>=3.6',
    install_requires=[
        #
    ],
)