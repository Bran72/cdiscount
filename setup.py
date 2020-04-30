import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='cdiscount',
    version='1.0.0',
    author="Brandon Leininger",
    author_email="brandon.leininger@icloud.com",
    description="A utility package to get any cdiscount product price",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bran72/cdiscount",
    packages=['cdiscount'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
