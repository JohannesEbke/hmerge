from setuptools import setup, find_packages

setup(
    name="hmerge",
    packages=find_packages(),
    entry_points={
        "console_scripts" : [
            "hmerge=hmerge:main",
        ]
    },
)
