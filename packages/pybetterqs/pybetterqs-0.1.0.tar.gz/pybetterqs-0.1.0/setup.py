from setuptools import setup, find_packages,extension

setup(
name='pybetterqs',
version='0.1.0',
author='blotterchains',
author_email='rezagina68@gmail.com',
description='betterqs wrapper for python using ffi.just send params to it and get json params.better qs is better than urllib parse_qs',
packages=find_packages(),
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
include_package_data=True,
package_data={"pybetterqs": ['libdor_qs.so']},
python_requires='>=3.6',
)