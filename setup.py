from setuptools import setup

setup(
    name='YahooFinanceQuery',
    url='https://github.com/KWYing/yf-query',
    author='zxbliz',
    author_email='zxbliz10@gmail.com',
    # Packages
    packages=['yfQuery'],
    # Dependencis
    install_requires=['pandas'],
    # Version
    version='0.1.1',
    # License
    license='MIT',
    description='Price data downloader for Yahoo Finance Query API',
    # Readme
    # long_description=open('README.md').read(),
)