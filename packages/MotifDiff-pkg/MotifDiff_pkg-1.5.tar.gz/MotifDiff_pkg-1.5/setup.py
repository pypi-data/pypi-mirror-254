from setuptools import setup, find_packages

setup(
    name='MotifDiff_pkg',
    version='1.5',
    packages=find_packages(),
    install_requires=[
        'typer',
        'torch',
        'numpy',
        'pandas',
        'pysam',
        'scipy',
        'regex',
    ],
    entry_points={
        'console_scripts': [
            'getDiff = MotifDiff:variantdiff',
        ],
    },
)
