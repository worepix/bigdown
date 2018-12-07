from setuptools import setup

setup(
	name="bigdown",
	version="1.0",
	py_modules=["app.countdown"],
	install_requires=[
		"DateTime",
		"Click",
        "simple-date",
        "paho-mqtt",
        ],
	entry_points='''
		[console_scripts]
		bigdown=app.countdown:cli
	'''
)
