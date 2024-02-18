from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()


setup(
  name='XlDemerge',
  version='0.1.0',
  packages = find_packages(),
  install_requires=[
    'openpyxl==3.1.2',
    'pandas==1.5.3',
    'numpy==1.23.5'
  ],
  long_description = description,
  long_description_content_type="text/markdown",
)