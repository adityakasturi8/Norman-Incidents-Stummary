from setuptools import setup, find_packages

setup(
    name='project0',
    version='1.0',
    author='Aditya Kasturi',
    author_email='adityakasturi@ou.edu',
    packages=find_packages(exclude=('tests', 'docs')),
    setup_requires=['pytest-runner'],
    tests_require=['pytest']    
    )
