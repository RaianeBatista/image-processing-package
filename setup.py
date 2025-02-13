from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirement.txt") as f:  # Alterado para "requirement.txt"
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Raiane_Batista",
    description="Image Processing Package using skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RaianeBatista/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
)