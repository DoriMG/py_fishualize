import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fishualize",
    version="0.0.11",
    author="Dori Grijseels",
    author_email="d.grijseels@sussex.ac.uk",
    description="Python version of the fishualize package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DoriMG/py_fishualize",
    packages=setuptools.find_packages(),
	install_requires=[
		'pandas>=0.19.0',
        'numpy>=1.13.0',
		'matplotlib>=2.0.0',
      ],
	include_package_data=True ,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
