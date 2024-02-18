from setuptools import setup,find_packages

with open("README.md",encoding="utf-8",mode="r")as f:
    long_description = f.read()

setup(
    name="formulite",
    version="0.0.3",
    description='Simple Formula Parser',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Tom0427',
    author_email='tom.ipynb@gmail.com',
    license='MIT',
    keywords='parser, formula, formulite',
    python_requires='>=3.10',
    packages=find_packages(),
    url="https://github.com/Tom-game-project/formulite"
)