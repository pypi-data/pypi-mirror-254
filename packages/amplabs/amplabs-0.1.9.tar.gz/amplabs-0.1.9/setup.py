from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='amplabs',
    packages=find_packages(),
    package_data={'assets': ['*']},
    version='0.1.9',
    description='One of the AmpLabs product to create high end plots for your data',
    author='Amplabs',
    install_requires=['dash','Pillow','dash-bootstrap-components'],
    readme = "README.md",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True
)