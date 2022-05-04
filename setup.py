import os
import re
import sys
import pathlib
from setuptools import setup

if sys.version_info < (3, 7):
    raise RuntimeError("Django API Proxy requires Python 3.7+")

HERE = pathlib.Path(__file__).parent

txt = (HERE / 'django_api_proxy' / '__init__.py').read_text('utf-8')
try:
    version = re.findall(r"^__version__ = '([^']+)'\r?$", txt, re.M)[0]
except IndexError:
    raise RuntimeError('Unable to determine version.')

with open(os.path.join(HERE, 'README.md')) as f:
    README = f.read()

setup(
    name='django-api-proxy',
    version=version,
    description='Django Rest Framework proxy API',
    long_description=README,
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Framework :: Django :: 3',
        'Framework :: Django :: 4',
    ],
    author='Alessio Pinna',
    author_email='alessio.pinna@aiselis.com',
    maintainer='Alessio Pinna <alessio.pinna@aiselis.com>',
    url='https://github.com/aiselis/django-api-proxy',
    project_urls={
        'Bug Reports': 'https://github.com/aiselis/django-api-proxy/issues',
        'Source': 'https://github.com/aiselis/django-api-proxy',
    },
    license='BSD',
    packages=['django_api_proxy'],
    python_requires='>=3.7',
    install_requires=[
        'django>=3.0',
        'requests>=2.10',
        'djangorestframework>=3.1',
        'urllib3>=1.20',
        'six>=1.10',
    ],
    include_package_data=True,
)
