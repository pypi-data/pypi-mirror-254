import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="LiveCap",
    version="0.2.0",
    author="Hongli Wen",
    author_email="whl2075928012@gmail.com",
    description="Nothing to see here.",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/MosRat/",
    packages=setuptools.find_packages(),
    install_requires=['opencv-python>=4.8.1.78', 'numpy>=1.26.3', 'winsdk'],
    install_package_data=True,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
)
