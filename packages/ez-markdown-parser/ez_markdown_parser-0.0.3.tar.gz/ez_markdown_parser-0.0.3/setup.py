from setuptools import setup, find_packages

with open("README.md", "r") as f:
    pypi_description = f.read()

setup(
    name='ez_markdown_parser',
    version='0.0.3',
    packages=find_packages(),
    long_description=pypi_description,
    long_description_content_type='text/markdown',
)

# To upload changes to pypi:
# Have installed packages from requirements.txt
# Upgrade Version in this file up there 
# Compile Package: python setup.py sdist bdist_wheel
# Publish it to pypi: twine upload dist/* (user: __token__ , pass=YOUR_API_TOKEN)
# Push code changes to github