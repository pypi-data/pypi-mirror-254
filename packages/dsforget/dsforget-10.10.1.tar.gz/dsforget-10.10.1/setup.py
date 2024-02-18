from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_desc = f.read()

setup(
    name='dsforget',
    version='10.10.1',
    author='Harisiva R G',
    author_email='harisivarg@gmail.com',
    description='A package to create a data science project structure',
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url='https://github.com/Harisiva-rg/dsforge',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[], 
    license="MIT",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",

)
