
from setuptools import find_packages, setup

setup(
	name="qcmapper",
	version='0.0.6',
	description='quantum circuit mapping',
	author='Yongsoo Hwang',
	install_requires=['simplejson', 
					  'networkx', 
					  'numpy', 
					  'qubitmapping',
					  'progress'],
	packages=find_packages(include=['qcmapper', 'qcmapper.*']),
	zip_safe=False,
	python_requires='>=3'
	)