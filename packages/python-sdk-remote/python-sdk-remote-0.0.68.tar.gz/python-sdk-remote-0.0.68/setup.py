import setuptools

# used by python -m build
# python -m build needs pyproject.toml or setup.py
setuptools.setup(
    name='python-sdk-remote',
    version='0.0.68',  # https://pypi.org/project/python-sdk-remote/
    author="Circles",
    author_email="info@circles.life",
    description="PyPI Package for Circles Python SDK Local Python",
    long_description="This is a package for sharing common functions used in different repositories",
    long_description_content_type="text/markdown",
    url="https://github.com/circles-zone/python-sdk-remote-python-package",
    packages=setuptools.find_packages(),
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: Other/Proprietary License",
         "Operating System :: OS Independent",
    ],
)
