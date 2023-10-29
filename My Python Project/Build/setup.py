from setuptools import setup, find_packages

setup(
    name='MyPythonProject',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'shelll_script = Calculator:main'
        ],
    },
)
