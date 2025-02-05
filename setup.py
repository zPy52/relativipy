from setuptools import setup, find_packages

setup(
    name="mylib",  # Replace with your library name
    version="0.1.0",  # Start with an initial version
    packages=find_packages(),  # Automatically find your packages
    install_requires=[
        "numpy>=1.18.0",          # Specify that numpy must be at least version 1.18.0
        "requests>=2.20.0,<3.0.0",  # Specify a range for requests
    ],
    extras_require={
        "dev": [
            "pytest",   # For running tests
            "sphinx",   # For generating documentation
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A brief description of mylib",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",  # Ensures PyPI renders Markdown correctly
    url="https://github.com/yourusername/mylib",  # Replace with your repository URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Adjust if using a different license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version requirement
)
