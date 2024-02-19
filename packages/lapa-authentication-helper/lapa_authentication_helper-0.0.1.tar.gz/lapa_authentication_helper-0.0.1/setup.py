from setuptools import find_packages, setup

package_name = "lapa_authentication_helper"

setup(
    name=package_name,
    version="0.0.1",
    packages=find_packages(),
    package_data={
        package_name: ["data/*"],
    },
    install_requires=["requests>=2.31.0"],
    author="Amish Palkar",
    author_email="amishpalkar302001@gmail.com",
    description="helper to access the authentication service.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url=f"https://github.com/thepmsquare/{package_name}",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
)
