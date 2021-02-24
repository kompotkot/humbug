from setuptools import find_packages, setup

long_description = ""
with open("README.md") as ifp:
    long_description = ifp.read()

setup(
    name="flypaper",
    version="0.1.1",
    packages=find_packages(),
    install_requires=["bugout"],
    extras_require={
        "dev": ["black", "mypy", "wheel"],
        "distribute": ["setuptools", "twine", "wheel"],
    },
    description="Flypaper: Do you build developer tools? Flypaper helps you know your users.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Bugout.dev",
    author_email="engineering@bugout.dev",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development :: Libraries",
    ],
    url="https://github.com/bugout-dev/flypaper",
)