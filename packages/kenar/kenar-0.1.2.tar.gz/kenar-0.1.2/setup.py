#!/usr/bin/env python
"""The setup and build script for the python-telegram-bot library."""
from pathlib import Path

from setuptools import find_packages, setup


def get_packages_requirements(raw=False):
    exclude = ["tests*"]
    packs = find_packages(exclude=exclude)

    return packs


def get_setup_kwargs(raw=False):
    """Builds a dictionary of kwargs for the setup function"""
    packages = get_packages_requirements(raw=raw)

    readme = Path(f'README.md')

    kwargs = dict(
        script_name=f"setup.py",
        name="kenar",
        version="0.1.2",
        author="Amir Ehsandar",
        author_email="amir.ehsandar@divar.ir",
        license="LGPLv3",
        url="https://divar.ir/kenar",
        project_urls={
            "Documentation": "https://github.com/divar-ir/kenar-docs",
            "Bug Tracker": "https://github.com/divar-ir/kenar-docs/issues",
            "Source Code": "https://github.com/divar-ir/kenar-api",
        },
        download_url=f"https://pypi.org/project/kenar/",
        keywords="python divar bot api wrapper",
        description="Kenar API wrapper | written in python",
        long_description=readme.read_text(),
        long_description_content_type="text/markdown",
        packages=packages,
        install_requires=[
            "httpx==0.26.0",
            "gunicorn==21.2.0",
            "pydantic==2.6.0",
        ],
        include_package_data=True,
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
            "Operating System :: OS Independent",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Communications :: Chat",
            "Topic :: Internet",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
        ],
        python_requires=">=3.10",
    )

    return kwargs


def main():
    setup(**get_setup_kwargs(raw=False))


if __name__ == "__main__":
    main()
