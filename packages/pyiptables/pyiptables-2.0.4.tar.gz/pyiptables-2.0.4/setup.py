from setuptools import setup

setup(
    name='pyiptables',
    version='2.0.4',
    author='Xizhen Du',
    author_email='xizhendu@gmail.com',
    url='https://github.com/xizhendu/iptables',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    description='Simple Python client library for Iptables',
    packages=['pyiptables'],
    install_requires=[
    ]
)
