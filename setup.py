from setuptools import setup, find_packages

setup(
    name = 'shbus',
    version = '1.0.0',
    keywords = ('pip', 'shanghai', 'realtime', 'bus'),
    description = 'Python implementation of Shanghai Bus App.',
    long_description = '「上海公交」APP 的 Python 实现。基本实现了 APP 中所有功能，如查询线路、实时公交等。',
    license = 'MIT Licence',

    url = 'https://boar.moe',
    author = 'hebingchang',
    author_email = 'hebingchang1@live.com',

    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = ['requests', 'pycrypto', 'protobuf']
)