import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="concrete_autoencoder_new",
    version="0.0.1",
    author="Muhammed Fatih Balin",
    author_email="m.f.balin@gmail.com",
    description="An implementation of Concrete Autoencoders",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mattlevy15/Concrete-Autoencoders/concrete_autoencoder_new",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['tensorflow'],
    python_requires='>=3',
)
