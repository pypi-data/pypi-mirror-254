from setuptools import setup, find_packages

with open("README.md", "r") as stream:
    long_description = stream.read()

setup(
    name = "AminoService",
    version = "1.0.11",
    url = "https://github.com/innocentzero143/AminoService",
    download_url = "https://github.com/innocentzero143/AminoService/archive/refs/heads/main.zip",
    license = "MIT",
    author = "innocentzero143",
    long_description=long_description,
    author_email = "innocentzero143@gmail.com",
    description = "A library to create Amino bots and scripts",
    long_description_content_type = "text/markdown",
    keywords = [
        "aminoapps",
        "AminoService"
        "amino",
        "amino-bot",
        "narvii",
        "api",
        "python",
        "python3",
        "python3.x",
        "innocent-zero"
    ],
    install_requires = [
        "setuptools",
        "requests",
        "six",
        "websockets",
        "websocket-client==1.3.1",
        "aiohttp"
    ],
    setup_requires = [
        "wheel"
    ],
    packages = find_packages()
)
