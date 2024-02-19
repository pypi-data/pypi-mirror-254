from setuptools import setup
import re

version = ''
with open('yagpapi/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

packages = [
    'yagpapi',
]

setup(
    name='yagpapi.py',
    url='https://github.com/gxskpo/yagpapi.py',
    version=version,
    license='MIT',
    description='Placeholder',
    packages=packages,
    python_requires='>=3.9.0',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)