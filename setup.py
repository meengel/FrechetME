from setuptools import setup, find_packages

setup(
    name = 'FrechetME',
    version = '0.0.1',
    python_requires = ">=3.8",
    install_requires = [
        "numpy",
        "torch",
    ],
    packages = find_packages(),
    author = "Michael Engel",
    author_email = "m.engel@tum.de"
)