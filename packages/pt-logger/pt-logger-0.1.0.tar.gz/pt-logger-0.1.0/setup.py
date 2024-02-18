import pathlib

import setuptools

setuptools.setup(
    name="pt-logger",
    version="0.1.0",
    description="A simple logger library for Python",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://helpsocialbot.xyz",
    author="pternali",
    author_email="patrizio.ternali15@gmail.com",
    license="The Unlicense",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.9",
        "Topic :: Utilities"
    ],
    python_requires=">=3.9",
    packages=setuptools.find_packages(),
    include_package_data=True
)
