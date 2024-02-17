import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="libppocr",
    version="0.4.1",
    author="Hongli Wen",
    author_email="whl2075928012@gmail.com",
    description="add douyin effect to image",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/MosRat/libppocr",
    packages=setuptools.find_packages(),
    install_requires=['Pillow>=5.1.0', 'numpy>=1.14.4'],
    install_package_data=True,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
