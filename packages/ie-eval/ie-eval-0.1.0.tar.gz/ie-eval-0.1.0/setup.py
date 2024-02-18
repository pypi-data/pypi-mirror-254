import re
from pathlib import Path

from setuptools import find_packages, setup

SUBMODULE_PATTERN = re.compile("-e ((?:(?!#egg=).)*)(?:#egg=)?(.*)")


def parse_requirements_line(line: str) -> str:
    # Special case for git requirements
    if line.startswith("git+http"):
        assert "@" in line, "Branch should be specified with suffix (ex: @master)"
        assert (
            "#egg=" in line
        ), "Package name should be specified with suffix (ex: #egg=kraken)"
        package_name: str = line.split("#egg=")[-1]
        return f"{package_name} @ {line}"
    # Special case for submodule requirements
    elif line.startswith("-e"):
        package_path, package_name = SUBMODULE_PATTERN.match(line).groups()
        package_path: Path = Path(package_path).resolve()
        # Package name is optional: use folder name by default
        return f"{package_name or package_path.name} @ file://{package_path}"
    else:
        return line


def parse_requirements(filename: str) -> list[str]:
    path = Path(__file__).parent.resolve() / filename
    assert path.exists(), f"Missing requirements: {path}"
    return list(
        map(parse_requirements_line, map(str.strip, path.read_text().splitlines())),
    )


setup(
    install_requires=parse_requirements("requirements.txt"),
    extras_require={
        "dev": ["pre-commit", "tox"],
        "docs": parse_requirements("doc-requirements.txt"),
    },
    packages=find_packages(),
)
