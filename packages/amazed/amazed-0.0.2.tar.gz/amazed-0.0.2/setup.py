import setuptools
import amazed

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="amazed",
    version=amazed.__version__,
    author="Peterca Adrian",
    author_email="adipeterca@gmail.com",
    description="amazed is a package meant for maze generation & solving.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adipeterca/amazed",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)