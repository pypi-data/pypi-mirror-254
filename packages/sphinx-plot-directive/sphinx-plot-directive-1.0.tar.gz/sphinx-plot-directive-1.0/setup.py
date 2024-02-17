#!/usr/bin/env python
from setuptools import setup

setup(
    name='sphinx-plot-directive',
    version='1.0',
    description='An extension providing a reStructuredText directive .. plot:: for including and displaying a plot in a Sphinx document.',
    long_description=open('README.rst').read(),
    url='https://github.com/guoyoooping/sphinx-plot-directive',
    author='Yongping Guo',
    author_email='guoyoooping@163.com',
    license='MIT',
    packages=['sphinx_plot_directive'],
    python_requires='>=3.7',
    install_requires=["docutils", "Pillow"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
