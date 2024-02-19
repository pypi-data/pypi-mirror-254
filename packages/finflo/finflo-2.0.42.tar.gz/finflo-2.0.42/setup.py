from setuptools import find_packages, setup


# read from README.RST
def readme():
    with open("readme.md") as f:
        return f.read()


# updated
setup(
    name="finflo",
    version="2.0.42",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Anand Raj",
    author_email="anandrajb@venzotechnologies.com",
    python_requires=">=3.8",
    packages=find_packages(),
    install_requires=["django", "djangorestframework"],
)
