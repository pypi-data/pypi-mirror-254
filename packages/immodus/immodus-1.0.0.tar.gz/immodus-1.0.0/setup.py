import setuptools

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="immodus",
    version="1.0.0",
    author="yvolkov",
    author_email="yvvvolkov@mail.ru",
    description="Image modifier by user settings.",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yvvolkov/ImModUS",
    packages=['immodus'],
    install_requires=['numpy'],
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)
