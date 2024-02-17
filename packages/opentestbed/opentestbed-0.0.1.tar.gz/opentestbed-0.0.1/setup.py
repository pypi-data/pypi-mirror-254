"""
To build distribution: python setup.py sdist bdist_wheel --universal
"""
import os
import setuptools
from version import Version

pkg_name = Version.package_name
version = Version.version
testbed_models_version = Version.testbed_models_version

# read long description from readme.md
base_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(base_dir, "readme.md")) as fd:
    long_description = fd.read()

with open("testbed-models-release", "w") as out:
    out.write("v" + testbed_models_version)

install_requires = []
with open(os.path.join(base_dir, "requirements.txt"), "r+") as fd:
    install_requires = fd.readlines()
    install_requires = install_requires[1:]

setuptools.setup(
    name=pkg_name,
    version=version,
    description="The Open testbed Python Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/open-traffic-generator/opentestbed",
    author="Open Traffic Generator",
    author_email="anish.gottapu@keysight.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing :: Traffic Generation",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    keywords="OTG testbed for testbed reservation",
    include_package_data=True,
    packages=[pkg_name],
    python_requires=">=2.7, <4",
    install_requires=install_requires,
)
