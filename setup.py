from setuptools import setup, find_packages

version = '2.0.0'

with open('README.rst') as myfile:
    readme = myfile.read()
with open('CONTRIBUTORS.rst') as myfile:
    contributors = myfile.read()
with open('CHANGES.rst') as myfile:
    changes = myfile.read()

long_description = (
    readme
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    contributors
    + '\n' +
    changes
    + '\n')

setup(name='collective.cookiecuttr',
      version=version,
      description="Integration package for cookiecuttr, european guidelines",
      long_description=long_description,
      # Get more strings from https://pypi.org/classifiers/
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        ],
      keywords='cookies',
      author='Franklin Kingma',
      author_email='franklin@fourdigits.nl',
      url='https://github.com/collective/collective.cookiecuttr',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective', ],
      include_package_data=True,
      zip_safe=False,
      # Py 3.6 is end of life, but I don't want to explicitly break it
      # by disallowing it here.
      python_requires=">=3.6",
      install_requires=[
          'setuptools',
          'plone.app.registry',
          'plone.app.layout',
          'plone.browserlayer',
          'collective.z3cform.datagridfield'
      ],
      extras_require={
          'test': [
              'plone.app.testing',
              'zope.testrunner',
          ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
