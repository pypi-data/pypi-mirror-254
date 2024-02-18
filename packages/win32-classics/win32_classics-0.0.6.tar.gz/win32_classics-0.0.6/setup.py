from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.0.6"
DESCRIPTION = "Simplify win32 actions"

# Setting up
setup(
    name="win32_classics",
    version=VERSION,
    author="André Herber",
    author_email="andre.herber.programming@gmail.com",
    # url="https://github.com/ICreedenI/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    # package_data={"": [""]},
    include_package_data=True,
    install_requires=["pywin32", "screeninfo", "colorful_terminal", "exception_details"],
    keywords=["python"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
