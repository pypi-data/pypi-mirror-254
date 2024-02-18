from setuptools import setup, find_packages

VERSION = "0.2.0"

setup(
    name = 'plinko',
    version = VERSION,
    author = 'Nat Hawkins, Mike Chappelow',
    author_email = 'nat.hawkins@kellogg.com, michael.chappelow@kellogg.com',
    description = 'Python equivalent to the internal R library, klink, for establishing remote connections to data sources',
    license = 'LICENSE.txt',
    packages = find_packages(),
    scripts = [],
    install_requires=[],
    url = 'https://pypi.org/project/plinko'
)