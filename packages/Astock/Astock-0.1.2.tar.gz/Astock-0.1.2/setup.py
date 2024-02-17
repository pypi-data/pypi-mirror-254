from setuptools import setup, find_packages
setup(
    name = 'Astock',
    version= '0.1.2',
    description='stock data analyse',
    author='Jopil',
    author_email='jopil@163.com',
    classifiers=['Programming Language :: Python'],
    license='',
    install_requires=['pandas>=1.3.5','numpy>=1.21.5','xlrd>=2.0.1'],
    packages=find_packages(),
    # packages=find_packages(where='library_manager'),
    # package_dir={'': 'library_lanager'},
    include_package_data=True
    # package_data={'':['*.csv','*.xlsx','*.xls']}
    
)