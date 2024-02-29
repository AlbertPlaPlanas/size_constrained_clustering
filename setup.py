from setuptools import find_packages, dist
from wheel.bdist_wheel import bdist_wheel

try:
    from setuptools import setup
except:
    from distutils.core import setup

import os

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

dist.Distribution().fetch_build_eggs(["numpy>=1.13"])

path = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(path, "requirements.txt")) as fp:
    install_requires = fp.read().strip().split("\n")


VERSION = "0.0.8.3"
LICENSE = "MIT"
setup(
    #ext_modules=extensions,
    version=VERSION,
    setup_requires=["numpy"],
    install_requires=install_requires,
    name="light_size_constrained_clustering",
    description="Size Constrained Clustering solver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlbertPlaPlanas/size_constrained_clustering",
    author="Albert Pla",
    author_email="plaalbert@gmail.com",
    license=LICENSE,
    packages=find_packages(),
    python_requires=">=3.6",
)
