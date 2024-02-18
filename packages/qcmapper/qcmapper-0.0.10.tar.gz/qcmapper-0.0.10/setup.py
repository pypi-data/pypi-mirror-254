
# -*-coding:utf-8-*-

# This code is part of qcmapper (quantum circuit mapper)
#
# Copyright 2022 ETRI
#
# This code is licensed under the BSD-3-Clause.

from setuptools import find_packages, setup

setup(
	name="qcmapper",
	version='0.0.10',
	description='quantum circuit mapper',
	author='Yongsoo Hwang',
	packages=find_packages(include=['library', 'library.*']),
	zip_safe=False,
	python_requires='>=3',
	install_requires=['simplejson',
					  'networkx',
					  'pandas',
					  'progress',
					  'icecream'],
	
	)