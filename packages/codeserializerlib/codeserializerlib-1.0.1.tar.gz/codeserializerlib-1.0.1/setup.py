from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('requirements-dev.txt') as f:
    dev_requirements = f.read().splitlines()

with open('README.md') as f:
    long_description = f.read()

setup(
    name='codeserializerlib',
    packages=find_packages(),
    version='1.0.1',
    description='Python library for the code serializer',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Tony Meissner',
    author_email="tonymeissner70@gmail.com",
    install_requires=requirements,
    extras_require={
        'dev': dev_requirements
    },
    package_data={
        '': ['codeserializerlib/model'],
    },
    include_package_data=True,
)