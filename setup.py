from setuptools import setup, find_packages

setup(
    name="flashmate",
    version="0.1.0",
    description="GUI tool for firmware file extraction from build archives",
    author="SeongYong Kim",
    author_email="seongyong.kim@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "PySide6>=6.5.0",
        "zipfile36>=0.1.3",
        "pathlib2>=2.3.7",
    ],
    extras_require={
        "dev": [
            "PyInstaller>=5.10.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "pre-commit>=3.0.0",
        ],
    },
) 