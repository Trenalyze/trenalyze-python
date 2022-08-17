import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="trenalyze-python",
    version="0.0.1",
    author="Treasure Uvietobore",
    author_email="uvietoboretreasure@gmail.com",
    packages=["trenalyze-python"],
    description="A Python package to send WhatsApp messages through Trenalyze",
    long_description=description,
    long_description_content_type="text/markdown",
    url="",
    license="MIT"
    python_requires=">=3.6",
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)