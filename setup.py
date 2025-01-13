#!/usr/bin/env python3

from setuptools import find_packages, setup, find_namespace_packages

setup(
    name='stpa',
    version='0.0.0',
    description='A Python framework for the digitalization of STPA for real-life systems',
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    url='https://github.com/blueskysolarracing/stpa',
    author='Blue Sky Solar Racing',
    author_email='blueskysolar@studentorg.utoronto.ca',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Education',
        'Topic :: Education :: Testing',
        'Topic :: Scientific/Engineering',
    ],
    keywords=[
        'mit',
        'stamp',
        'stpa',
    ],
    project_urls={
        'Documentation': 'https://stpa.readthedocs.io/en/latest/',
        'Source': 'https://github.com/blueskysolarracing/stpa',
        'Tracker': 'https://github.com/blueskysolarracing/stpa/issues',
    },
    packages=find_packages(),
    python_requires='>=3.11',
    package_data={'stpa': ['py.typed']},
)
