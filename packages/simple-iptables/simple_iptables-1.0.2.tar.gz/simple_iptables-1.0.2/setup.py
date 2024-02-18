from setuptools import setup

setup(
    name='simple_iptables',
    version='1.0.2',
    author='Xizhen Du',
    author_email='xizhendu@gmail.com',
    url='https://github.com/xizhendu/iptables',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    description='Simple Python client library for Iptables',
    packages=['simple_iptables'],
    install_requires=[
    ]
)
