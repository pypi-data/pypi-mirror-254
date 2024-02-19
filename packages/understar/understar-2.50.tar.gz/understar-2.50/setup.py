from setuptools import setup, find_packages

with open("README.md", "r") as stream:
    long_description = stream.read()

with open("understar/.version", "r") as stream:
    version = stream.read().strip()  # Assurez-vous de supprimer les éventuels espaces ou retours à la ligne

setup(
    name='understar',
    version=version,
    url='https://github.com/GalTechDev/UnderStar-OS',
    download_url='https://github.com/GalTechDev/UnderStar-OS/tarball/master',
    license='MIT',
    author='GalTech',
    author_email='poussigalitv@gmail.com',
    description='A discord bot framework',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=[
        "discord",
        "bot",
        "discord.py",
        "understar",
        "os",
        "framework"
    ],
    install_requires=[
        "easy-events>=2.9.0",
        "discord.py>=2.1",
        "requests_html",
    ],
    setup_requires=[
        'wheel'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    package_data={"understar": [".version"]},
    python_requires='>=3.10',
)
