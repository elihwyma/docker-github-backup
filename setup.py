from setuptools import setup

setup(
    name='github-backup',
    version='1.0.0',
    description='',
    url='https://github.com/elihwyma/docker-github-backup',
    author='elihwyma',
    install_requires=['requests'],
    scripts=['github-backup.py'],
    zip_safe=True
)
