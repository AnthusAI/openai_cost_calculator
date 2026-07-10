import re
from pathlib import Path

from setuptools import find_packages, setup


ROOT = Path(__file__).parent
README = ROOT / "README.md"
VERSION_FILE = ROOT / "openai_cost_calculator" / "_version.py"


def package_version() -> str:
    match = re.search(
        r'^__version__ = "([^"]+)"',
        VERSION_FILE.read_text(),
        re.MULTILINE,
    )
    if not match:
        raise RuntimeError("Unable to read package version")
    return match.group(1)


setup(
    name="openai_cost_calculator",
    version=package_version(),
    description="Calculate model usage costs from token counts",
    long_description=README.read_text() if README.exists() else "",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.8",
)
