from setuptools import setup, find_packages

VERSION = '0.0.9'
DESCRIPTION = 'Cyclic redundancy check for the given data bits'
LONG_DESCRIPTION = 'A simple cyclic redundancy script which can take dividend and divisor as input and perform xor long division, encode it, decode it and finally tells whether there is any loss in transfer of data by checking the syndrome.'

# Setting up
setup(
    name="cyclicredundancypython",
    version=VERSION,
    scripts=['src/cyc.py'],
    author="Thejas hari",
    author_email="<thejaskala308@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
     entry_points={
        'console_scripts': [
            'cyc = src.cyc:main',
        ],
    },
    install_requires=[],
    keywords=['python', 'url', 'cyclic-redundance', 'encode','decode','cyc','cyc-encode-decode'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)