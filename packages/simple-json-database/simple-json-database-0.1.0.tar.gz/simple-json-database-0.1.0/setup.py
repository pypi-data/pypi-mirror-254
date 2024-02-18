from setuptools import setup, find_packages

# with open("README.rst", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setup(
    name="simple-json-database",
    version="0.1.0",
    author="Emil Tsaturyan",
    author_email="emiltsaturyan60@gmail.com",
    description="Simple json database",
    # long_description=long_description,
    # long_description_content_type="text/x-rst",
    url="https://github.com/EmilTsaturyan/json-db",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.0",
    keywords=['python', 'json', 'database', 'csv']
)
