from setuptools import setup


setup(
	name="bigsegment",
	version="1.0",
	py_modules=["Countdown"],
	install_requires=[
		"DateTime",
		"Click",
        "simple-date",
        "paho-mqtt",
        ],
	entry_points='''
		[console_scripts]
		bigsegment=countdown:cli
	'''
)