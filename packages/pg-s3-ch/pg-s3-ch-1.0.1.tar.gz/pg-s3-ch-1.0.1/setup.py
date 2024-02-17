from setuptools import setup, find_packages


def load_requirements(file_name):
    requirements = []
    with open(file_name, "r") as file:
        for line in file:
            # Remove comments and strip whitespace
            line = line.split("#")[0].strip()
            if line:
                requirements.append(line)
    return requirements


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pg-s3-ch',
    packages=find_packages(),
    version='1.0.1',
    license='MIT',
    description='PG S3 CH Helper',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Dmitry Utiralov',
    author_email='d.utiralov@netology.tech',
    url='https://github.com/severgroup-tt/topmind-commons',
    install_requires=load_requirements("requirements.txt"),
    extras_require={
        "dev": load_requirements("dev-requirements.txt"),
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.9'
)
