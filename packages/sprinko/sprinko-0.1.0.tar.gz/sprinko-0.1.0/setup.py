from setuptools import setup

setup(
    name="sprinko",
    version="0.1.0",
    packages=[
        "sprinko._cli",
        "sprinko._cli_bottler",
        "sprinko.core",
        "sprinko.base",
        "sprinko.extra",
    ],
    install_requires=[
        "requests",
        "click",
        "orjson",
        "parse",
        "toml",
        "tabulate",
        "prompt-toolkit",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "sprinko=sprinko._cli.__main__:bowl_",
            "sprinko-bottler=sprinko._cli_bottler.__main__:bottler_cli",
        ]
    },
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)