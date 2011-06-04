from setuptools import setup, find_packages

setup(
    name="hmerge",
    py_modules=["hmerge"],
    entry_points={
        "console_scripts" : [
            "hmerge=hmerge:main",
        ]
    },
)
