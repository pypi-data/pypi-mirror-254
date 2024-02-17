from setuptools import setup
from setuptools import find_packages

with open("Readme.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()

docs_require = [
    "Markdown==3.3.7",
    "markdown-include==0.7.0",
    "MarkupSafe==2.1.1",
    "mkdocs==1.3.1",
    "mkdocs-autorefs==0.4.1",
    "mkdocs-git-revision-date-localized-plugin==1.1.0",
    "mkdocs-include-markdown-plugin==3.8.1",
    "mkdocs-material==8.5.3",
    "mkdocs-material-extensions==1.0.3",
    "mkdocstrings==0.19.0",
    "mkdocstrings-python==0.7.1",
    "Pygments==2.13.0",
    "pymdown-extensions==9.5",
]

tests_require = [
    "coverage==6.4.4",
    "coverage-badge==1.1.0",
    "griffe==0.22.1",
    "pytest==7.1.3",
    "pytest-cov==3.0.0",
]

build_require = ["setuptools==65.3.0"]

all_requirements = required + docs_require + tests_require + build_require

setup(
    name="steam-sdk",
    version="2024.1.3",
    author="STEAM Team",
    author_email="steam-team@cern.ch",
    description="Source code for APIs for STEAM tools.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.cern.ch/steam/steam_sdk",
    keywords={"STEAM", "API", "SDK", "CERN"},
    install_requires=required,
    extras_require={
        "all": all_requirements,
        "docs": docs_require,
        "tests": tests_require,
        "build": build_require,
    },
    python_requires=">=3.8",
    include_package_data=True,
    packages=find_packages(),
    classifiers=["Programming Language :: Python :: 3.8"],
)
