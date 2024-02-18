from setuptools import setup

setup(
    name='trendpy2',
    version='1.0.2',    
    description='Time series regression with python',
    url='https://github.com/zolabar/trendPy/tree/main',
    author='Zoufiné Lauer-Baré',
    license='MIT License',
    packages=['trendpy2'],
    install_requires=[
    'numpy',
    'scipy',
    'sympy ',
                      ],


    
    )