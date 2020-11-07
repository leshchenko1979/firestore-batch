import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="firestore_batch",
    version="0.0.1",
    author="Alexey Leshchenko",
    author_email="leshchenko@gmail.com",
    description="A simple Python context manager for easy Google Forestore batched writes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leshchenko1979/firestore-batch",
    packages=['firestore_batch'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=None,
    license="MIT"
)