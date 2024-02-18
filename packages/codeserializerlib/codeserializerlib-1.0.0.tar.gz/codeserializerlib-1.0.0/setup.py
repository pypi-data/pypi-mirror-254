from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('requirements-dev.txt') as f:
    dev_requirements = f.read().splitlines()

setup(
    name='codeserializerlib',
    packages=find_packages(),
    version='1.0.0',
    description='Python library for the code serializer',
    author='Tony Meissner',
    install_requires=requirements,
    extras_require={
        'dev': dev_requirements
    },
    package_data={
        '': ['codeserializerlib/model'],
    },
    include_package_data=True,
)