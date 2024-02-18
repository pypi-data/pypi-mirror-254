from setuptools import setup, find_packages


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()


setup(
    name="procesadortext",
    version="1.0",
    packages=find_packages(include=['procesamiento', 'procesamiento.*']),
    url="",
    author="Carlos Estrada",
    description="This is my text processor that will process text using 9 NLP processing tehcniques and two display",
    long_description=read_file(file_name="README.md"),
    long_description_content_type="text/markdown",
    python_requires=">=3.11",
    install_requires=[
        'pandas==2.1.4',
        'pytest==6.2.4',
        'nltk==3.6.5',
        'setuptools==69.0.2',
        'jupyter==1.0.0',
        'matplotlib==3.8.2',
        'spacy==3.7.2',
        'wordcloud==1.9.3'
    ]
)
