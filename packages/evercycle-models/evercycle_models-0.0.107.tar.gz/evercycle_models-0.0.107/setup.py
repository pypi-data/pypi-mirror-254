from setuptools import setup

setup(
    name='evercycle_models',
    version='0.0.107',
    packages=[
        'evercycle_models',
        'evercycle_models.models',
        'evercycle_models.migrations',
        'evercycle_models.utils'
    ],
    include_package_data=True,
    license='MIT',
    description='Application to be used in any Evercycle Microservice',
    author='Evercycle',
    author_email='admin@evercycle.io',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'Django>=3.0',
    ],
)
