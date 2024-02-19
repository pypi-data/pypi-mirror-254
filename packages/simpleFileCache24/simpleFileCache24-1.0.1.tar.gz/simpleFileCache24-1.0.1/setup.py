from setuptools import setup

setup(
    name='simpleFileCache24',
    version='1.0.1',
    author='zackaryW',
    install_requires=['cryptography', 'keyring', 'requests', 'sioDict'],
    packages=[
        'simpleFileCache',
        'simpleFileCache.utils',
    ],
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown"
)