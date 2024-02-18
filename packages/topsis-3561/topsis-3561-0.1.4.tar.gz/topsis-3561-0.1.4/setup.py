from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

DESCRIPTION = 'Implementation of Topsis'

setup(
    name='topsis-3561',
    version='0.1.4',
    author="Mannat Sadana",
    author_email="sadana.mannat@gmail.com",
    license='MIT License',
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pandas','numpy'],
    project_urls={
        'Project Link': 'https://github.com/moxie814/Topsis-102103561.git'
    },
)
