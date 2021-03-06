import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "snoopy",
    version = "0.0.1",
    author = "Adam Ballai",
    author_email = "aballai@gmail.com",
    description = ("Snoopy sleeps on his house."),
    license = "Mine",
    keywords = "house sleepy snoopy better-than-the-flintstones",
    setup_requires=['nose>=1.0', 'Flask>=0.10.1', 'kafka-python==0.9.3', 'gevent'],
    packages=['snoopy', 'snoopy.connection', 'tests'],
	entry_points = {
		'console_scripts': ['snoopyd=snoopy.server:start_server'],
    },
    long_description=read('README')
)
