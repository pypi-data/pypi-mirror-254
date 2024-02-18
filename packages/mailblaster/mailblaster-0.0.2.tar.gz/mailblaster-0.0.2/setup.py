from setuptools import setup, find_packages

setup(
    name='mailblaster',
    version='0.0.2',
    description='Send many emails from many accounts',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='prim4t',
    author_email = "python@prim4t.art",
    url='https://github.com/prim4t/mailblaster',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here

    ],
)
