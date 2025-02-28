import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()


__version__="0.0.0"
REPO_NAME="text_summarization"
SRC_REPO="textSummarization"
AUTHOR_NAME="Zahid"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)