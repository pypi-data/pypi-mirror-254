from setuptools import setup, find_packages

setup(
    name='MotifDiff-pkg',
    version='0.2',
    packages=find_packages(),
    install_requires=[
    	'torch',
    	'pandas',
        'util',
        'numpy',
        'enum',
        'typer',
        'pickle',
        'time',
        'pysam',
        'itertools',
        'scipy',
        'regex',
        'xml'
    ],
    entry_points={
        'console_scripts': [
            'getDiff = MotifDiff.MotifDiff.py:variantdiff',
        ],
    },
)
