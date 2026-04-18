from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="code-roaster",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="AI-powered code review with attitude",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/code-roaster",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Quality Assurance",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "ollama>=0.1.0",
    ],
    entry_points={
        "console_scripts": [
            "roaster=roaster:main",
        ],
    },
)
