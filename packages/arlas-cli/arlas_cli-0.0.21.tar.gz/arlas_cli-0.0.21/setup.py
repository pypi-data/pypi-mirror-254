import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arlas_cli",
    entry_points={'console_scripts': ['arlas_cli=arlas.cli.cli:main']},
    version="0.0.21",
    author="Gisaïa",
    description="ARLAS Command line for collection management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires='>=3.11',
    py_modules=["arlas.cli.cli", "arlas.cli.collections", "arlas.cli.index", "arlas.cli.settings", "arlas.cli.variables", "arlas.cli.service"],
    package_dir={'': 'src'},
    install_requires=[]
)
