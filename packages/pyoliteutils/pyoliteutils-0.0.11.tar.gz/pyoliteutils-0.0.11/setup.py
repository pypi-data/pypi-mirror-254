import setuptools
import versioneer

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

setuptools.setup(
    name="pyoliteutils",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Marty Eggleton @ UTC Sheffield OLP",
    author_email="meggleton@utcsheffield.org.uk",
    description="Utils for making pyolite easier to use inside MS Teams notebooks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
)
