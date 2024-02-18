# from setuptools import setup
#
# setup(
#     name='mymodules',
#     version='4.0',
#     packages=['''Xbyte_Common_Scrape'''],
# )

from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '7.0.4'
DESCRIPTION = 'use for easy scraping'
LONG_DESCRIPTION = 'scraping'

# Setting up
setup(
    name="mymodules",
    version=VERSION,
    author="XBYTE",
    author_email="<mail@neuralnine.com>",
    description="Simple helping tool for scraping",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=['''Xbyte_Common_Scrape'''],
    install_requires=[],
    keywords=['json', 'pymysql', 'requests', 'random_user_agent'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)