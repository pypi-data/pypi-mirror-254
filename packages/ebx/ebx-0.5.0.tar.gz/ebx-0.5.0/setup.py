from setuptools import setup, find_packages

NAME = "ebx"
VERSION = "0.5.0"

REQUIRES = [
    "pydantic >= 2.1.1",
    "geojson-pydantic >= 1.0.0",
    "pandas >= 2.0.0",
    "httpx >= 0.24.1",
    "leafmap >= 0.23.3",
    "plotly >= 5.16.1"
]

setup(
    name=NAME,
    version=VERSION,
    description="Earth Blox Client API",
    author_email="j.wilkins@earthblox.io",
    url="https://earthblox.io/",
    keywords=["Earth Blox", "geospatial"],
    install_requires=REQUIRES,
    packages=find_packages("ebx"),
    include_package_data=True,
)
