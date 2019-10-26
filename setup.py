import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py fishualize",
    version="0.0.6",
    author="Dori Grijseels",
    author_email="d.grijseels@sussex.ac.uk",
    description="Python version of the fishualize package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DoriekeG/py_fishualize",
    packages=setuptools.find_packages(),
	install_requires=[
		'pandas>=0.19.0',
        'numpy>=1.13.0',
		'matplotlib>=2.0.0',

      ],
	include_package_data=True ,
    classifiers=[
        "Programming Language :: Python :: 3",
        "LICENSE :: OSI APPROVED :: GNU GENERAL PUBLIC LICENSE V3 (GPLV3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',


)
