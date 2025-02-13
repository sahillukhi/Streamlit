from setuptools import setup, find_packages

setup(
    name="Text Summerizer and Question Answer chat bot",
    version="0.0.1",
    author="Sahil Lukhi",
    author_email="sahillukhi9@gmail.com",
    install_requires=[
        "langchain",
        "openai",
        "pinecone-client",
        "pypdf",
        "python-dotenv",
        "langchain-community",
        "ai21"
    ],
    packages=find_packages(),
)
