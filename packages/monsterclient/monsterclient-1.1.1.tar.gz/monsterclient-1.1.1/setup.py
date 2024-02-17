from setuptools import setup, find_packages

# Read the content of your README file
with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="monsterclient",
    version="1.1.1",
    description="client for monster",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["requests", "click", "pygments", "bs4"],
    entry_points="""
      [console_scripts]
      monster=monsterclient.monster:main
      """,
)
