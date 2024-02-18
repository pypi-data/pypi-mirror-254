
from setuptools import find_packages, setup

setup(
	name="qcmapper",
	version='0.0.8',
	description='quantum circuit mapper',
	author='Yongsoo Hwang',
	packages=find_packages(include=['library', 'library.*']),
	zip_safe=False,
	python_requires='>=3',
	install_requires=['simplejson',
					  'networkx',
					  'progress'],
	
	)