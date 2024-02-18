from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="streamlit_modal_input",
    version="0.0.11",
    author="Baptiste Ferrand",
    author_email="bferrand.math@gmail.com",
    description="Modal text input component for Streamlit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/B4PT0R/streamlit_modal_input",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.9",
    install_requires=[
        "streamlit >= 1.30",
        "firebase-user"
    ],
)
