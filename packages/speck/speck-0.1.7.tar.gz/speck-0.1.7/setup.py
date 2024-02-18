from setuptools import find_packages, setup


def readme():
    with open("README.md") as f:
        README = f.read()
    return README


def parse_requirements(filename):
    with open(filename, "r") as f:
        requirements = f.read().splitlines()
    return requirements


install_requires = [
    "openai",
    "replicate",
    "requests",
    "pydantic",
    "httpx",
    "websockets",
    "litellm",
]


setup(
    name="speck",
    packages=find_packages(exclude=["tests", "tests.*"]),
    version="0.1.7",
    description="Speck - Development and observability toolkit for LLM apps.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords=[
        "speck",
        "openai",
        "llm",
        "ai",
        "chat",
        "bot",
        "gpt",
        "gpt-3",
        "gpt-4",
        "anthropic",
        "replicate",
        "litellm",
        "observability",
    ],
    url="https://github.com/speckai/speck",
    download_url="https://github.com/speckai/speck/archive/refs/tags/v0.1.7.tar.gz",
    homepage="https://getspeck.ai",
    author="",
    author_email="Lucas Jaggernauth <luke@getspeck.ai>, Raghav Pillai <raghav@getspeck.ai>",
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
    ],
    include_package_data=True,
    install_requires=install_requires,
)
