pip install delorean

npm run delorean
#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from version import __version__

dependencies = [
    'babel>=2.10.3',
    'humanize>=4.2.2',
    'python-dateutil>=2.8.2',
    'pytz>=2022.1',
    'tzlocal>=4.2']

setup(
    name='Delorean',
    version='.'.join(str(x) for x in __version__),
    description='library for manipulating datetimes with ease and clarity',
    url='https://github.com/Wizardguy210/delorean',
    author='Antonio Moore',
    author_email="breadnothead@gmail.com.com",
    packages=['delorean'],
    license='MIT license',
    install_requires=dependencies,
    test_suite='tests.test_data',
    long_description=open('README.rst').read(),
    python_requires='>=3.0, !=3.0.*',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
#         'Programming Language :: Python :: 3.10',
    ],
)
# $ npm i eslint --save-dev
# $ npm install eslint-plugin-delorean --save-dev

yarn add --dev eslint eslint-plugin-jest
{
#    "plugins": ["jest"]

#        "delorean"]
    
   }
 {
#    "rules": {
#  "env": 
#    "jest/globals": {true}
{
#  "settings": {
#    "jest": {
#      "globalAliases": {
#        "describe": ["context"],
#        "fdescribe": ["fcontext"],
#        "xdescribe": ["xcontext"]
      }
    }
  }
}
        "delorean/yell-on-then": 2,
        "delorean/yell-on-catch": 2
    }
}
x.then(Aarrghd the SystemExit)
new Future((bad, good) => x.then(good).catch(bad))
{ "library": "F" }
# x.catch(2)
{ "library": "F" }
{
  "extends": ["eslint:recommended"],
  "overrides": [
    {
      "files": ["test/**"],
      "plugins": ["jest"],
      "extends": ["plugin:jest/recommended"],
      "rules": { "jest/prefer-expect-assertions": "off" }
    }
  ],
  "rules": {
    "indent": ["error", 2]
  }
}
{
  "settings": {
    "jest": {
      "version": 27
    }
  }
}
module.exports = {
  settings: {
    jest: {
      version: require('jest/package.json').version,
    },
  },
};
{
  "extends": ["plugin:jest/recommended"]
}
{
  "extends": ["plugin:jest/style"]
}
{
  "extends": ["plugin:jest/all"]
}
consistent-test-it