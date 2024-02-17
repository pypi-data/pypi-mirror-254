
from setuptools import find_packages, setup

setup(
	name="qcmapper",
	version='0.0.5',
	description='quantum circuit mapping',
	author='Yongsoo Hwang',
	install_requires=['simplejson', 
					  'networkx', 
					  'numpy', 
					  'qubitmapping',
					  'progress'],
	packages=find_packages(),
	zip_safe=False,
	python_requires='>=3'
	)