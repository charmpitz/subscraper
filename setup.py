from setuptools import setup

setup(name='subscraper',
	scripts=['bin/subscraper'],
	version='0.4',
	description='Movies/Series Subtitle Downloader',
	url='http://github.com/charmpitz/subscraper',
	author='Andrei Pit',
	author_email='charmpitz@gmail.com',
	license='MIT',
	packages=['subscraper', 'requests', 'pycurl', 'bs4'],
	zip_safe=False)