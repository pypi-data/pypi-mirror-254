from distutils.core import setup
from os.path import abspath, dirname, join

README_MD = open(join(dirname(abspath(__file__)), "README.md")).read()

setup(
    name='lvldb',
    version='0.1.1',
    keywords="Python, LevelDB",
    description='Python bindings for LevelDB. Python 2-3 compatible',
    long_description=README_MD,
    long_description_content_type="text/plain",
    author='JT Olds',
    author_email='jt@spacemonkey.com',
    url="https://github.com/jtolio/leveldb-py",
    py_modules = ["lvldb"])
