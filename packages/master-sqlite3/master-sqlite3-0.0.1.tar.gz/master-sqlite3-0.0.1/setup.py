from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='master-sqlite3',
    version='0.0.1',
    license='MIT License',
    author='Ryan Souza Anselmo',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='ryansouza.cwb@gmail.com',
    keywords='master sqlite3',
    description=u'The Master SQLite3 library is a powerful and easy-to-use tool that significantly simplifies interaction with SQLite databases in Python.',
    packages=['Master_SQLite3'],
    install_requires=[''],)