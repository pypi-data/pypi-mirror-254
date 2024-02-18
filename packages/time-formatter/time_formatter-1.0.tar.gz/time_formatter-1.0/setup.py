from setuptools import setup, find_packages

# Dane projektu
project_name = "time_formatter"
project_version = "1.0"
project_description = "Universal time formatter, from seconds to %H:%M:%S format"
project_author = "PanSage_"
project_author_email = "root@pansage.xyz"

# Zależności
dependencies = [
]

# Odczytaj zawartość README.md jako długopis
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name=project_name,
    version=project_version,
    author=project_author,
    author_email=project_author_email,
    description=project_description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PanSageYT/time_formatter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=dependencies
)
