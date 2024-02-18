from setuptools import setup, find_packages

setup(
    name='MotifDiff',
    version='1.2',
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
            'varDiff = MotifDiff:variantdiff',
        ],
    },
)
