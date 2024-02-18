
#
#	https://setuptools.pypa.io/en/latest/userguide/quickstart.html
#
#	https://github.com/pypa/sampleproject/blob/db5806e0a3204034c51b1c00dde7d5eb3fa2532e/setup.py
#
from setuptools import setup, find_packages

version = "1.0.5"
name = 'body_scan'
install_requires = [ 
	'botanist',
	
	'click',
	'flask',
	'pdoc3',
	'requests',
	'textual',
	'tinydb'
]

def scan_description ():
	try:
		with open ('module.txt') as f:
			return f.read ()
				
	except Exception as E:
			pass;
		
	return '';

setup (
    name = name,
    version = version,
    install_requires = install_requires,	
	
	package_dir = { 
		name: 'structure/decor/' + name
	},
	
	#
	#
	include_package_data = True,
	package_data = {
		"": [ "*.PY" ]
    },
	
	
	license = "GPL 3.0",
	
	project_urls = {
		"GitLab": "https://gitlab.com/reptilian_climates/body_scan.git"
	},
	
	long_description = scan_description (),
	#long_description_content_type = "text/markdown",
	long_description_content_type = "text/plain"
)