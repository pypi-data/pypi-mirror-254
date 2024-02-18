
#
#	https://setuptools.pypa.io/en/latest/userguide/quickstart.html
#

from setuptools import setup, find_packages

name = 'botanist'

description = ''
try:
	with open ('botanist.s.HTML') as f:
		description = f.read ()

except Exception as E:
	pass;

setup (
    name = name,
    version = '1.0.0',
    install_requires = [
		'psutil'
	],	
	package_dir = { name: 'fields/gardens/' + name },
	
	license = "GPL 3.0",
	long_description = description,
	long_description_content_type = "text/plain"
	
	
	#package_data = {
	#	NAME: [ 'DATA/**/*' ]
	#}
)