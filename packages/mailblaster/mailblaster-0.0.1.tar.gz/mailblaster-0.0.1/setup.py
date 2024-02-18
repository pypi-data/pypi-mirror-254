from setuptools import setup, find_packages

setup(
    name='mailblaster',
    version='0.0.1',
    description='Send many emails from many accounts',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='prim4t',
    author_email = "python@prim4t.art",
    url='https://github.com/your_username/your_package',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        'smtplib',
        'email',
    ],
)
