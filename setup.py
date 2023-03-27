from setuptools import setup

from src import __version__

setup(
    name='supported_languages',
    version=__version__,

    url='https://github.com/thesocialcoin/supported_languages',
    author='Oscar Delgado',
    author_email='odelgado@citibeats.com',

    py_modules=['src.countries', 'src.languages'],
)
