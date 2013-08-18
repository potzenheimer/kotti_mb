import os

from setuptools import find_packages
from setuptools import setup

version = '1.0'
project = 'kotti_mb'

install_requires=[
        'Kotti',
    ],

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

setup(name=project,
      version=version,
      description="AddOn for Kotti",
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "License :: Repoze Public License",
        ],
      keywords='kotti addon',
      author='Christoph Boehner',
      author_email='cb@vorwaerts-werbung.de',
      url='http://pypi.python.org/pypi/',
      license='bsd',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=[],
      entry_points={
        'fanstatic.libraries': [
          'kotti_mb = kotti_mb.fanstatic:library',
        ],
      },
      extras_require={},
      message_extractors={'kotti_mb': [
            ('**.py', 'lingua_python', None),
            ('**.zcml', 'lingua_xml', None),
            ('**.pt', 'lingua_xml', None),
            ]},
      )
