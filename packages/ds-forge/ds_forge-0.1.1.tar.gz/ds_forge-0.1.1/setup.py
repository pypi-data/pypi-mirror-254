from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_desc = f.read()

setup(
    name='ds_forge',
    version='0.1.1',
    author='Harisiva R G',
    author_email='harisivarg@gmail.com',
    description='A package to create a data science project structure',
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url='https://github.com/Harisiva-rg/ds_forge',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['logging'], 
    entry_points={
        'console_scripts': [
            'template=template:main',
        ],
    },
)
