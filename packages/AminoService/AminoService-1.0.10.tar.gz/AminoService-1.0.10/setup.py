from setuptools import setup, find_packages


setup(
    name = "AminoService",
    version = "1.0.10",
    url = "https://github.com/",
    download_url = "https://github.com/",
    license = "MIT",
    author = "INNOCENT_ZERO",
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
    include_package_data=True,
    packages = find_packages()

)


