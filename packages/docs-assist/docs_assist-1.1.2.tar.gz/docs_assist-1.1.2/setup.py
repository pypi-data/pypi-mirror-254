from setuptools import find_packages, setup
setup(
    name='docs_assist',
    packages=find_packages(include=['docs_assist']),
    version='1.1.2',
    description='An Assistant API based on OpenAI Modern Assistant API. It accepts a document and answer the questions based on the document uploaded.',
    author='Muhammad Asif Ali',
    install_requires=['openai']

)

