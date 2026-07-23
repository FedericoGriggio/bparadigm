from pathlib import Path

from setuptools import find_packages, setup

requirements = Path(__file__).parent.joinpath("requirements.txt").read_text().splitlines()
requirements = [r.strip() for r in requirements if r.strip() and not r.startswith("#")]

setup(
    name="bparadigm",
    version="0.1.0",
    description="AI-powered competitor intelligence through transformer-based NLP.",
    packages=find_packages(include=["bparadigm", "baradigm.*"]),
    install_requires=requirements,
    python_requires=">=3.10",
)
