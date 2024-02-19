from setuptools import setup, find_packages
import os
import codecs

def read_file(filepath):
    """Read content from a UTF-8 encoded text file."""
    with codecs.open(filepath, "rb", "utf-8") as file_handle:
        return file_handle.read()

VERSION = '0.0.1.beta'
DESCRIPTION = 'Xcaliber Webhooks'
# LONG_DESCRIPTION = ''
PKG_README = read_file(os.path.join(os.path.dirname(__file__), "README.md"))

# Setting up
setup(
    name="xcaliber_webhooks",
    version=VERSION,
    # author="",
    # author_email="",
    description=DESCRIPTION,
    # long_description_content_type="text/markdown",
    # long_description=long_description,
    packages=find_packages(),
    install_requires=['svix'],
    keywords=['xcaliber','webhooks'],
    long_description=PKG_README,
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)