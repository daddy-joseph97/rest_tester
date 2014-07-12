""" Setup file.
"""
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()

install_requires=[
    'requests',
    'nose',
    'mock',
    ]

setup(name='rest_tester',
    version=0.1,
    description='rest_tester',
    long_description=README,
    classifiers=[
        "Programming Language :: Python",
    ],
    keywords="testing",
    author='',
    author_email='',
    url='',
    packages=find_packages(),
    #tests_require=tests_require,
    #extras_require = {
        #'testing':testing_extras,
        #'docs':docs_extras,
        #},
    test_suite='rest_tester.tests',
)