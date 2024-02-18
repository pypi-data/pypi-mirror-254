import os
import setuptools


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        content = file.read()
    return content


setuptools.setup(
    name="bibrecord",
    version=read("VERSION").strip(),
    description="Handling bibliographic records within source code",
    long_description=read("README.rst"),
    long_description_content_type="text/x-rst",
    author="Till Biskup",
    author_email="till@till-biskup.de",
    url="",
    project_urls={
        "Documentation": "https://bibrecord.docs.till-biskup.de/",
        "Source": "https://github.com/tillbiskup/bibrecord",
    },
    packages=setuptools.find_packages(exclude=("tests", "docs")),
    license="BSD",
    keywords=[
        "bibliography",
        "bibtex",
        "literature",
        "cite",
        "references",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Development Status :: 4 - Beta",
    ],
    install_requires=[],
    extras_require={
        "dev": [
            "prospector",
            "pyroma",
            "bandit",
            "black",
            "pymetacode",
        ],
        "docs": [
            "sphinx",
            "sphinx-rtd-theme",
            "sphinx_multiversion",
        ],
        "deployment": [
            "build",
            "twine",
        ],
    },
    python_requires=">=3.7",
    include_package_data=True,
)
