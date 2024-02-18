import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "idev-pipall",
    version = "1.0.0",
    author = "IrtsaDevelopment",
    author_email = "irtsa.development@gmail.com",
    description = "A python script for executing pip commands across many or all packages.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/IrtsaDevelopment/pipall",
    project_urls = {
        "Bug Tracker": "https://github.com/IrtsaDevelopment/pipall/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': ['pipall = pipall:run'] 
    },
    package_dir = {"": "idev-pipall"},
    packages = ["pipall"],
    install_requires = "idev-pytermcolor",
    python_requires = ">=3.6"
)