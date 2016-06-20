from setuptools import setup, find_packages
import re


def get_version(filename="django_nvd3/__init__.py", varname="__version__"):
    glb = {}
    with open(filename) as fp:
        for line in fp:
            if varname in line:
                exec(line, glb)
                break
    return glb[varname]


def readfile(filename):
    with open(filename) as fp:
        return fp.read()


readme = readfile('README.rst')
history = readfile('CHANGELOG.rst').replace('.. :changelog:', '')


setup(
    name='django-nvd3',
    version=get_version(),
    description="Django NVD3 - Chart Library for d3.js",
    long_description=readme + '\n\n' + history,
    keywords='django, nvd3, chart, graph, d3',
    url='http://github.com/areski/django-nvd3',
    author='Belaid Arezqui',
    author_email='areski@gmail.com',
    license='MIT',
    zip_safe=False,
    packages=["django_nvd3"],
    install_requires=["Django", "python-nvd3"],
    test_suite='tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
