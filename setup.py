import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="trenalyze_python",
    version="0.0.3",
    author="Treasure Uvietobore",
    author_email="uvietoboretreasure@gmail.com",
    packages=["trenalyze_python"],
    description="A Python package to send WhatsApp messages through Trenalyze",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/Trenalyze/trenalyze_python",
    license="MIT",
    python_requires=">=3.6",
    install_requires=["requests", "json"]
)