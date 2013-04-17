from setuptools import setup, find_packages
import django_nvd3
import os
import codecs
import re


def read(*parts):
    return codecs.open(os.path.join(os.path.dirname(__file__), *parts)).read()


def parse_requirements(file_name):
    requirements = []
    for line in open(file_name, 'r').read().split('\n'):
        if re.match(r'(\s*#)|(\s*$)', line):
            continue
        if re.match(r'\s*-e\s+', line):
            requirements.append(re.sub(r'\s*-e\s+.*#egg=(.*)$', r'\1', line))
        elif re.match(r'(\s*git)|(\s*hg)', line):
            pass
        else:
            requirements.append(line)
    return requirements


def parse_dependency_links(file_name):
    dependency_links = []
    for line in open(file_name, 'r').read().split('\n'):
        if re.match(r'\s*-[ef]\s+', line):
            dependency_links.append(re.sub(r'\s*-[ef]\s+', '', line))

    return dependency_links


setup(
    name='django-nvd3',
    version=django_nvd3.__version__,
    description='django application to display graph with NVD3',
    long_description=read('README.rst'),
    keywords='django, nvd3, chart, graph, d3',
    url='http://github.com/areski/django-nvd3',
    author='Belaid Arezqui',
    author_email='areski@gmail.com',
    license='MIT License',
    zip_safe=False,
    packages=find_packages(exclude=["tests", "demoproject", "docs"]),
    include_package_data=True,
    package_data={},
    install_requires=parse_requirements('requirements.txt'),
    dependency_links=parse_dependency_links('requirements.txt'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
