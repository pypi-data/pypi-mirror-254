#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pipenv install twine --dev

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command
# python setup.py sdist bdist_wheel
# twine upload dist/*
# Package meta-data.
NAME = 'spider_tools'
DESCRIPTION = 'My short description for my project.'
URL = 'https://github.com/me/myproject'
EMAIL = '597854439@qq.com'
AUTHOR = 'zcl'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.4.1'

# What packages are required for this module to be executed?
REQUIRED = [
    # 'requests', 'maya', 'records',
    'aliyun-python-sdk-core==2.14.0',
    'aliyun-python-sdk-kms==2.16.2'             ,
    'arrow==1.3.0'                              ,
    'async-timeout==4.0.3'                      ,
    'attrs==23.2.0'                             ,
    'Automat==22.10.0'                          ,
    'certifi==2023.11.17'                       ,
    'cffi==1.16.0'                              ,
    'chardet==5.2.0'                            ,
    'charset-normalizer==3.3.2'                 ,
    'colorama==0.4.6'                           ,
    'constantly==23.10.4'                       ,
    'crcmod==1.7'                               ,
    'cryptography==42.0.1'                      ,
    'cssselect==1.2.0'                          ,
    'DBUtils==1.3'                              ,
    'docutils==0.20.1'                          ,
    'exceptiongroup==1.2.0'                     ,
    'filelock==3.13.1'                          ,
    'h11==0.14.0'                               ,
    'hyperlink==21.0.0'                         ,
    'idna==3.6'                                 ,
    'importlib-metadata==7.0.1'                 ,
    'importlib-resources==6.1.1'                ,
    'incremental==22.10.0'                      ,
    'itemadapter==0.8.0'                        ,
    'itemloaders==1.1.0'                        ,
    'jaraco.classes==3.3.0'                     ,
    'jieba==0.42.1'                             ,
    'jmespath==0.10.0'                          ,
    'keyring==24.3.0'                           ,
    'loguru==0.7.2'                             ,
    'lxml==5.1.0'                               ,
    'markdown-it-py==3.0.0'                     ,
    'mdurl==0.1.2'                              ,
    'more-itertools==10.2.0'                    ,
    'nh3==0.2.15'                               ,
    'numpy==1.24.4'                             ,
    'oss2==2.18.4'                              ,
    'outcome==1.3.0.post0'                      ,
    'packaging==23.2'                           ,
    'parsel==1.8.1'                             ,
    'pillow==10.2.0'                            ,
    'pkginfo==1.9.6'                            ,
    'Protego==0.3.0'                            ,
    'pyasn1==0.5.1'                             ,
    'pyasn1-modules==0.3.0'                     ,
    'pycparser==2.21'                           ,
    'pycryptodome==3.20.0'                      ,
    'PyDispatcher==2.0.7'                       ,
    'PyExecJS==1.5.1'                           ,
    'pyforest==1.1.0'                           ,
    'Pygments==2.17.2'                          ,
    'PyMySQL==1.1.0'                            ,
    'pyOpenSSL==24.0.0'                         ,
    'PySocks==1.7.1'                            ,
    'pytesseract==0.3.10'                       ,
    'python-dateutil==2.8.2'                    ,
    'pywin32-ctypes==0.2.2'                     ,
    'queuelib==1.6.2'                           ,
    'readme-renderer==42.0'                     ,
    'redis==5.0.1'                              ,
    'requests==2.31.0'                          ,
    'requests-file==1.5.1'                      ,
    'requests-toolbelt==1.0.0'                  ,
    'rfc3986==2.0.0'                            ,
    'rich==13.7.0'                              ,
    'Scrapy==2.11.0'                            ,
    'selenium==4.17.2'                          ,
    'service-identity==24.1.0'                  ,
    'six==1.16.0'                               ,
    'sniffio==1.3.0'                            ,
    'sortedcontainers==2.4.0'                   ,
    'spider_tools==0.4.0'                       ,
    'tldextract==5.1.1'                         ,
    'tqdm==4.66.1'                              ,
    'trio==0.24.0'                              ,
    'trio-websocket==0.11.1'                    ,
    'twine==4.0.2'                              ,
    'Twisted==22.10.0'                          ,
    'twisted-iocpsupport==1.0.4'                ,
    'types-python-dateutil==2.8.19.20240106'    ,
    'typing_extensions==4.9.0'                  ,
    'urllib3==2.2.0'                            ,
    'w3lib==2.1.2'                              ,
    'win32-setctime==1.1.0'                     ,
    'wsproto==1.2.0'                            ,
    'xlrd==2.0.1'                               ,
    'zipp==3.17.0'                              ,
    'zope.interface==6.1'                       ,

]

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()


# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
)
