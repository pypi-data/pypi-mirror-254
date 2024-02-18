# setup.py
"""
This module is used for setting up the package distribution. It defines the package metadata,
reads the package version from a file, and specifies dependencies and other configurations 
necessary for packaging and distribution.
"""

from setuptools import setup, find_packages


# Function to read the version from _version.py
def get_version(rel_path):
    """
    Reads the version string from a given file.

    This function opens the file specified by `rel_path` and scans it for a line starting with
    "__version__". It then parses and returns the version string found in this line.

    Parameters:
    rel_path (str): A relative path to the file containing the version string.

    Returns:
    str: The version string if found.

    Raises:
    RuntimeError: If the version string is not found in the file.
    """
    with open(rel_path, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("__version__"):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


# Get version
version = get_version("src/google_text_to_speech/_version.py")

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="google_text_to_speech",
    version=version,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    description="A text-to-speech conversion tool using Google Translate API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Momcilo Krunic",
    author_email="momcilo.krunic@labsoft.ai",
    url="https://gitlab.com/labsoft-ai/google-translate-tts",
    license="MIT",
    install_requires=["requests", "playsound"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
