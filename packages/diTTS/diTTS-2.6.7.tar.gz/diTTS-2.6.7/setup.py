from setuptools import setup, find_packages
import os

version_py = os.path.join(os.path.dirname(__file__), "ditts", "version.py")
version = open(version_py).read().strip().split("=")[-1].replace('"', "").strip()

setup(
    name="diTTS",
    packages=find_packages(),
    python_requires=">=3.7",
    include_package_data=True,
    install_requires=[
        "requests >=2.27, <3",  # https://docs.python-requests.org/en/latest/community/updates/
        "click >=7.1, <8.2",    # https://click.palletsprojects.com/en/latest/changes/
    ],
    extras_require={
        "test" : [
            "pytest >= 7.1.3,< 8.1.0",
            "pytest-cov",
            "testfixtures",
        ]
    },
    entry_points={"console_scripts": ["ditts-cli=ditts.cli:tts_cli"]},
    description="diTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate text-to-speech API",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="blket.dev",
    author_email="blket.dev@gmail.com",
    url="https://github.com/blket.dev/diTTS",
    version=version,
    test_suite="gitts.tests",
    keywords=[
        "ditts",
        "text to speech",
        "NAVER Papago",
        "TTS",
    ],
    classifiers = [
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
    ],
    license="MIT",
)