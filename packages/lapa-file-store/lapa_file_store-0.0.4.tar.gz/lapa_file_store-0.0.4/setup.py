from setuptools import find_packages, setup

package_name = "lapa_file_store"

setup(
    name=package_name,
    version="0.0.4",
    packages=find_packages(),
    package_data={
        package_name: ["data/*", "pydantic_models/*"],
    },
    install_requires=[
        "uvicorn>=0.24.0.post1",
        "fastapi>=0.104.1",
        "python-multipart>=0.0.6",
        "square_logger~=1.0",
        "pydantic>=2.5.3",
        "lapa_database_helper>=0.0.3",
    ],
    author="Aaditya sangishetty, thePmSquare",
    author_email="adityashetty35@gmail.com, thepmsquare@gmail.com",
    description="file storage layer for my personal server.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url=f"https://github.com/adityashetty35/{package_name}",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
)
