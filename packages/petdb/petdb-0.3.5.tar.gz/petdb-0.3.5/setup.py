from setuptools import setup

setup(
	name="petdb",
	version="0.3.5",
	description="Light weight local document-oriented database.",
	long_description=open("README.md").read(),
	long_description_content_type="text/markdown",
	url="https://gitlab.com/Tullp/petdb",
	author="Maks Vinnytskyi",
	license_file="LICENSE",
	packages=["petdb"],
)
