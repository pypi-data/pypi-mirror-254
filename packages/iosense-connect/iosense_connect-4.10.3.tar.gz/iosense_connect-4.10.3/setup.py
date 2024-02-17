import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "iosense_connect",
    version = "4.10.3",
    author = "Faclon-Labs",
    author_email = "reachus@faclon.com",
    description = "iosense connect library",
    packages = ["iosense_connect"],
    long_description = long_description,
    long_description_content_type = "text/markdown",
    install_requires=[
        'cryptography',
        'fsspec',
        'numpy',
        'pandas',
        'python_dateutil',
        'Requests',
        'urllib3',
        'pyarrow',
        'azure-storage-blob>=12.16',
        'adlfs',
        'azure-core',
        'azure-datalake-store',
        'azure-identity',
        'botocore',
        'gcsfs',
        's3fs',
    ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
