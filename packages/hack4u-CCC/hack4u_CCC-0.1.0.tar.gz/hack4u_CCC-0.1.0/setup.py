from setuptools import setup, find_packages

#Leer el contenido del archivo Readme.md
with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

setup(
	name = "hack4u_CCC",
	version = "0.1.0",
	packages = find_packages(),
	install_requires = [],
	author = "Cesar Corregidor",
	description = "Una biblioteca para consultar cursos de hack4u.",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	url = "https://hack4u.io"
)
