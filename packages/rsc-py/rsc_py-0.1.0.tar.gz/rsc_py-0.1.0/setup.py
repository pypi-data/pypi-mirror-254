from setuptools import setup, find_packages

setup(
    name="rsc_py",
    version="0.1.0",
    author="deffuseyou",
    author_email="kriulindmitry@mail.ru",
    description="A library for controlling PowerPoint via Remote Show Control using Python",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/deffuseyou/rsc_py",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
