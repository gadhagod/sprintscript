
import setuptools

setuptools.setup(
    name='sprintscript',
    version='1.0.0.0',
    author='Aarav Borthakur',
    author_email='gadhaguy13@gmail.com',
    description='A command line utility that simplifies repetitive commands for any kind of scripting. ',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gadhagod/sprintscript',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'colorama',
    ],
    scripts=['./run'],
    python_requires='>=3.6'
)