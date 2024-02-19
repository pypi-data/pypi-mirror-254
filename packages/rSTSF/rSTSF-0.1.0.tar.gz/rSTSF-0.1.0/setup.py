from setuptools import setup, find_packages

setup(
    name='rSTSF',
    version='0.1.0',
    author='Nestor Cabello',
    author_email='stevcabello@gmail.com',
    packages=find_packages(),
    description='Fast, accurate and explainable time series classification through randomization',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'numpy', 'pandas', 'scikit-learn', 'scipy', 'numba', 'pyfftw', 'matplotlib', 'statsmodels', 'warnings'  # List all your dependencies
    ],
    url='https://github.com/stevcabello/r-STSF',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
