import setuptools

with open('./README.md', 'r') as fh:
    long_description = fh.read()
    
setuptools.setup(name="python-GUAGOD-setup",  # Replace with your own username
    version="0.0.1",
    author="liangjie",
    author_email="605564874@qq.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zjZSTU/aaa.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6')