from setuptools import setup, find_packages

setup(
    name='cook_containers',
    version='0.1',
    packages=find_packages(),
    install_requires=[
       'ruamel.yaml<0.18.0'

    ],
    entry_points={
        'console_scripts': [
            'cook-containers=cook_containers.main:main',
        ],
    },
)
