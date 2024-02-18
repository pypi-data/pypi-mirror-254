#!/usr/bin/env python3

from setuptools import setup

with open('README.md', 'r') as f:
	readme = f.read()

setup(
	# First, state all metadata about the package.
	name='simexpal',
	version='1.1',
	description='Tool to Simplify Experimental Algorithmics',
	url='https://github.com/hu-macsy/simexpal',
	author='Florian Willich',
	author_email='florian.willich@informatik.hu-berlin.de',
	license='MIT',
	long_description=readme,
	long_description_content_type='text/markdown',

	# Now, set the actual Python configuration.
	packages=['simexpal', 'simexpal.launch'],
	package_data={'simexpal': ['schemes/*.json']},
	scripts=['scripts/simex'],
	install_requires=[
		'importlib-metadata<5.0',
		'argcomplete',
		'requests',
		'pyyaml',
		'jsonschema>=3.2.0'
	]
)

