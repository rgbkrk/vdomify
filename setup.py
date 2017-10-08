#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python


from os.path import exists
from setuptools import setup
import versioneer

import sys

setup(name='vdomify',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='vdomify objects',
      author='nteract contributors',
      author_email='jupyter@googlegroups.com',
      license='BSD',
      keywords="vdom, html",
      long_description=(open('README.md').read() if exists('README.md') else ''),
      url='https://github.com/rgbkrk/vdomify',
      packages=['vdomify'],
      install_requires=[
          'vdom'
      ],
     )
