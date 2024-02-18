from setuptools import setup, find_packages

requirements = [
    "requests",
    "websocket-client==1.3.1", 
    "setuptools", 
    "json_minify", 
    "six",
    "aiohttp",
    "websockets",
    "pydantic==1.10.7"
]

with open("README.md", "r") as stream:
    long_description = stream.read()

setup(
    name="new-edamino",
    license="MIT",
    author="Lucas",
    version="1.4",
    author_email="lucasday173@gmail.com",
    description="Library for Amino.",
    url="https://github.com/LucasAlgerDay/new-edamino",
    packages=find_packages(),
    long_description=long_description,
    install_requires=requirements,
    keywords=[
        'aminoapps',
        'edamino',
        'amino',
        'amino-bot',
        'narvii',
        'api',
        'python',
        'python3',
        'python3.x'
    ],
    python_requires='>=3.6',
)