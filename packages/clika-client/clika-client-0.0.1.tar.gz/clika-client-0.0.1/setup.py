import os
import sys
import codecs
import fileinput
import shutil
from pathlib import Path
from contextlib import contextmanager

from setuptools import setup

BASE_DIR: Path = Path(__file__).parent

print(sys.argv)
if len(sys.argv) < 3:
    raise RuntimeError("Bad parameters to build the package")

ACTION: str = sys.argv[1]
PACKAGE_NAME: str = sys.argv[2]
PACKAGE_VERSION: str = "0.0.1"

sys.argv.remove(PACKAGE_NAME)

ERROR_MSG: str = """


###########################################################################################
*** WARNING ***
The package you are trying to install is only a placeholder project on PyPI.org repository.
This package is hosted on CLIKA Python Package Index to which you would need a license key to download.

Please visit us at www.clika.io
###########################################################################################


"""
README_MD: str = f"""
{PACKAGE_NAME}
=====================

**WARNING:** The package you are trying to install is only a placeholder project on PyPI.org repository.
This package is hosted on CLIKA Python Package Index to which you would need a license key to download.

Please visit us at www.clika.io
"""



def main():
    global ACTION, PACKAGE_NAME, PACKAGE_VERSION
    classifiers = [
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ]

    setup(
        name=PACKAGE_NAME,
        version=PACKAGE_VERSION,
        description="A fake package to warn the user they are not installing the correct package.",
        long_description=README_MD,
        long_description_content_type="text/markdown",

        # The project's main homepage.
        url="https://www.clika.io",
        # download_url="www.clika.io",

        # Author details
        author="CLIKA Inc.",
        author_email="support@clika.io",

        # maintainer Details
        maintainer='CLIKA Inc.',
        maintainer_email='support@clika.io',

        # The licence under which the project is released
        # license="Apache2",
        classifiers=classifiers,
        platforms=["Linux"],
        license="Proprietary",
        keywords=["compression", "neural networks", "quantization", "pruning", "clika", "llm", "transformer", "vision", "generative", "edge"],
    )


if ACTION == "sdist":
    main()
else:
    raise RuntimeError(ERROR_MSG)

