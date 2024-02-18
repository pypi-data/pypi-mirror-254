from setuptools import find_packages
from setuptools import setup

setup(
    name="Bard-Img",
    version="0.0.1",
    license="GNU General Public License v2.0",
    author="Talaviya Bhavik",
    author_email="talaviyabhavik@proton.me",
    description="High quality image generation by Microsoft Designer. Reverse engineered API.",
    packages=find_packages("bard-img"),
    package_dir={"": "bard-img"},
    url="https://github.com/imnotdev25/Bard-Image",
    project_urls={
        "Bug Report": "https://github.com/imnotdev25/Bard-Image/issues/new",
    },
    install_requires=[
        "httpx",
        ""
    ],
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    py_modules=["Bard-Img"],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
