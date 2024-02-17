from setuptools import setup

with open("README.md", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name="uuid-v9",
    version="0.1.1",
    author="JHunt",
    author_email="hello@jhunt.dev",
    description="Fast, lightweight, and dependency-free implementation of the UUID version 9 proposal for Python.",
    long_description=readme,
    long_description_content_type="text/markdown",
    # url="https://uuid-v9.jhunt.dev",
    packages=["."],
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires=">=3.8",
    platforms="any",
)
