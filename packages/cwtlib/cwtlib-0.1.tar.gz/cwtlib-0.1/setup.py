from setuptools import setup, find_packages

setup(
    name="cwtlib",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'numpy>=1.18.1',
        'requests>=2.22.0',
    ],
    # другие метаданные:
    author="Dmitrii Babaev",
    author_email="babaevdmitri@gmail.com",
    description="A package for working with the basic calculations of the CWT, RO",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/fscontrol/cwtlib",
)
