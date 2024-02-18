from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

VERSION = '1.0.6'
DESCRIPTION = 'Implementation of Topsis'

setup(
    name="Topsis-Naman-102116058",
    version=VERSION,
    author="Naman Bhargava",
    author_email="nambhargava03@gmail.com",
    license='MIT License',
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pandas','numpy'],
    project_urls={
        'Project Link': 'https://github.com/bravo003/Topsis-Naman-102116058'
    },
   
     classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]
)