from setuptools import setup,find_packages

with open("README.md","r") as f:
    description=f.read()
setup(
    name='EPICGAMES_FREE_PURCHASE',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'beautifulsoup4',
    ],
    entry_points={
        "console_scripts": [
            "EPICGAMES_START=EpicGames_FreeGames_Bot:start"
        ],
    },
    long_description=description,
    long_description_content_type="text/markdown",
)