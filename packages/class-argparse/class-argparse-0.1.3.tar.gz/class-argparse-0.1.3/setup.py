import os
import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="class-argparse",
    packages=["class_argparse"],
    version=os.environ["RELEASE_VERSION"],
    license="MIT",
    description="Class based argument parser",
    author="Neblar",
    author_email="support@neblar.com",
    url="https://github.com/neblar/class-argparse",
    keywords=["Class Based", "CLI", "Argparse"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
)
