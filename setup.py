import pathlib

__import__("setuptools").setup(
    name="blackletters",
    version="0.0.0",
    include_package_data=True,
    install_requires=pathlib.Path("requirements.txt").read_text().splitlines(),
)