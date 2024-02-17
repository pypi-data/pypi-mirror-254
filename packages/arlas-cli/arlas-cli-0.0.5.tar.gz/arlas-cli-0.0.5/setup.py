import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arlas-cli",
    scripts=['bin/arlas-cli'],
    version="0.0.5",
    author="Gisaïa",
    description="ARLAS Command line for collection management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires='>=3.11',
    py_modules=["arlas.cli"],
    package_dir={'': 'src'},
    install_requires=[]
)
