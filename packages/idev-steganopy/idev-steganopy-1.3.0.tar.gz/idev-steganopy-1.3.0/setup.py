import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "idev-steganopy",
    version = "1.3.0",
    author = "IrtsaDevelopment",
    author_email = "irtsa.development@gmail.com",
    description = "A python script for hiding text into images (steganography).",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/IrtsaDevelopment/Steganopy",
    project_urls = {
        "Bug Tracker": "https://github.com/IrtsaDevelopment/Steganopy/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': ['steganopy = Steganopy:run'] 
    },
    package_dir = {"": "idev-steganopy"},
    packages = ["Steganopy"],
    install_requires = "idev-pytermcolor",
    python_requires = ">=3.6"
)